// Original visual phrase control.
function phraseControl(){
 const duration=24, radius=8;
 const knots=[[0,32,72],[6,56,48],[12,80,72],[18,104,96],[24,128,72]];
 function pose(t){const i=Math.min(3,Math.floor(t/6)),a=knots[i],b=knots[i+1],u=(t-a[0])/6;return {x:a[1]+(b[1]-a[1])*u,y:a[2]+(b[2]-a[2])*u};}
 const variants=[{id:"canon",delay:6,kind:"copy"},{id:"crowded",delay:2,kind:"copy"},{id:"mirrored",delay:6,kind:"mirror"},{id:"diminished",delay:6,kind:"fast"}];
 const rows=variants.map(v=>{
 const frames=Array.from({length:42},(_,t)=>({t,voices:Array.from({length:3},(_,i)=>{let u=t-i*v.delay;if(i===1&&v.kind==="fast")u*=2;if(u<0||u>=duration)return null;const p=pose(u);return {voice:i,local:u,x:p.x,y:i===1&&v.kind==="mirror"?144-p.y:p.y};}).filter(Boolean)}));
 let min=Infinity,overlap=0,multi=0,three=0;
 for(const f of frames){let collision=false; if(f.voices.length>=2)multi++;if(f.voices.length===3)three++;for(let i=0;i<f.voices.length;i++)for(let j=i+1;j<f.voices.length;j++){const a=f.voices[i],b=f.voices[j],d=Math.hypot(a.x-b.x,a.y-b.y);min=Math.min(d,min);if(d<2*radius)collision=true;}if(collision)overlap++;}
 return {...v,min_center_distance:Number(min.toFixed(3)),overlap_ticks:overlap,multi_voice_ticks:multi,three_voice_ticks:three,frames};
 });
 const expected=(f,v)=>f.voices.every(o=>{let u=f.t-o.voice*v.delay;if(o.voice===1&&v.kind==="fast")u*=2;const p=pose(u);return o.local===u && o.x===p.x&&o.y===(o.voice===1&&v.kind==="mirror"?144-p.y:p.y)});
 const checks={all_voices_share_phrase:rows.every(v=>v.frames.every(f=>expected(f,v))),untransformed_canon_no_sample_overlap:rows[0].overlap_ticks===0,crowded_control_overlaps:rows[1].overlap_ticks>0,mirror_x_separation_preserved:rows[2].min_center_distance>=24,fast_variant_ends_earlier:rows[3].frames.filter(f=>f.voices.some(v=>v.voice===1)).length===12,simultaneous_voices:rows.every(r=>r.three_voice_ticks>0)};
 if(!Object.values(checks).every(Boolean))throw Error(JSON.stringify({checks,rows:rows.map(({frames,...r})=>r)}));
 return {hz:24,duration,radius,knots,rows,checks};
}
console.log(JSON.stringify(phraseControl(),null,2));
