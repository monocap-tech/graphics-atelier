// Original abstract event score and categorical control.
function scoreControl(){
 const hz=24,durationTicks=96,voice="AABABBAB".split("");
 const audio=voice.map((v,i)=>({id:i+1,tick:3+i*12,voice:v}));
 const map={A:"square",B:"ring"};
 const make=(id,seq,lag=0)=>({id,visual:seq.split("").map((v,i)=>({id:i+1,tick:audio[i].tick+lag,motif:map[v],duration:6}))});
 const variants=[make("declared_mapping","AABABBAB"),make("global_reassignment","BBABAABA"),make("inconsistent_reassignment","ABBBAAAB"),make("delayed_mapping","AABABBAB",3)];
 const rows=variants.map(v=>{
   const visual=v.visual;const aCount=visual.filter(x=>x.motif==="square").length;
   const matrix={A:{square:0,ring:0},B:{square:0,ring:0}};
   let aligned=0,lagSum=0,match=0;
   for(const x of audio){const y=visual.find(z=>z.id===x.id);matrix[x.voice][y.motif]++;if(y.tick===x.tick)aligned++;lagSum+=Math.abs(y.tick-x.tick);if(y.motif===map[x.voice])match++}
   return {id:v.id,events:visual.length,exact_onsets:aligned,mean_absolute_lag_ticks:lagSum/audio.length,declared_matches:match,best_bijective_matches:Math.max(match,audio.length-match),motif_counts:{square:aCount,ring:visual.length-aCount},matrix,inside_duration:visual.every(x=>x.tick>=0&&x.tick+x.duration<=durationTicks)};
 });
 const checks={same_counts:rows.every(x=>x.events===8&&x.motif_counts.square===4&&x.motif_counts.ring===4),same_synchrony_different_mapping:rows.slice(0,3).every(x=>x.exact_onsets===8)&&rows[0].declared_matches===8&&rows[2].declared_matches===4,alternative_consistent:rows[1].declared_matches===0&&rows[1].best_bijective_matches===8,irregular_mapping:rows[2].best_bijective_matches===4,lag_independent:rows[3].exact_onsets===0&&rows[3].declared_matches===8&&rows[3].mean_absolute_lag_ticks===3,all_inside:rows.every(x=>x.inside_duration)};
 if(!Object.values(checks).every(Boolean))throw Error(JSON.stringify({rows,checks}));return {hz,durationTicks,audio,variants,rows,checks};
}
console.log(JSON.stringify(scoreControl(),null,2));
