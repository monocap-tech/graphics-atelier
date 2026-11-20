// Original scalar compositing fixture, not an Effekseer or Unity renderer test.
function effectsControl(){
 const clip=x=>Math.min(1,Math.max(0,x));
 const over=(bg,c,a)=>c*a+(1-a)*bg;
 const backgrounds=[0,.2,.4,.6];
 const opacity=.25, normal=.4, emission=.35;
 const premultipliedNormal=normal*opacity, transmission=1-opacity;
 const samples=backgrounds.map(bg=>({background:bg,live:over(bg,normal,opacity)+emission,split:premultipliedNormal+transmission*bg+emission,normalOnlyMax:over(bg,1,opacity)}));
 const slope=(samples[3].live-samples[0].live)/.6, inferredAlpha=1-slope,inferredColor=samples[0].live/inferredAlpha;
 const rows=[.12,.5,.75].flatMap(bg=>[0,.35,.75].map(glow=>{
   const b=.86, cap=.35;
   const neighbor=clip(bg+glow);
   const front=clip(b+glow), behind=b, limitedNeighbor=Math.min(cap,neighbor);
   return {background:bg,glow,front_signed_difference:front-neighbor,behind_signed_difference:behind-neighbor,budgeted_signed_difference:behind-limitedNeighbor};
 }));
 const round=x=>Number(x.toFixed(9));
 const checks={split_matches:samples.every(x=>Math.abs(x.live-x.split)<1e-12),all_unclipped:samples.every(x=>x.live<=1),single_normal_requires_out_of_range_color:inferredColor>1,foreground_can_erase_difference:rows.some(x=>Math.abs(x.front_signed_difference)<1e-12),behind_not_sufficient:rows.some(x=>x.behind_signed_difference<=0),budgeted_positive_for_fixture:rows.every(x=>x.budgeted_signed_difference>=.51-1e-12)};
 if(!Object.values(checks).every(Boolean))throw Error(JSON.stringify(checks));
 return {samples:samples.map(r=>Object.fromEntries(Object.entries(r).map(([k,v])=>[k,round(v)]))),inferredAlpha:round(inferredAlpha),inferredColor:round(inferredColor),rows:rows.map(r=>Object.fromEntries(Object.entries(r).map(([k,v])=>[k,round(v)]))),checks};
}
console.log(JSON.stringify(effectsControl(),null,2));
