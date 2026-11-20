// Evaluate in a browser page already loaded with preview.html.
() => {
 const rows=[], canvas=document.getElementById('stage'), ctx=canvas.getContext('2d');
 for(const context of ['abstract','discharge','targeting'])for(const mode of ['continuous','stepped'])for(const cancel of [false,true]){
  let active=0,wrong=0,blockViolations=0;
  for(let t=0;t<48;t++){
   const p=renderAt(context,mode,t,cancel);active+=p.active;wrong+=p.active!==(!cancel&&t>=18&&t<30);
   if(t===22){const d=ctx.getImageData(0,0,640,360).data;for(let y=0;y<360;y+=4)for(let x=0;x<640;x+=4){let diff=false;const i=(y*640+x)*4;for(let dy=0;dy<4;dy++)for(let dx=0;dx<4;dx++){const j=((y+dy)*640+x+dx)*4;for(let c=0;c<4;c++)if(d[i+c]!==d[j+c])diff=true;}blockViolations+=diff;}}
  } rows.push({context,mode,cancel,activeTicks:active,wrong,blockViolations});
 }
 const samples=[];for(const mode of ['continuous','stepped'])for(const cancel of [false,true]){renderAt('discharge',mode,22,cancel);samples.push({mode,cancel,rgba:Array.from(ctx.getImageData(320,180,1,1).data)});}
 if(!rows.every(r=>r.wrong===0&&r.activeTicks===(r.cancel?0:12)&&(r.mode==='stepped'?r.blockViolations===0:r.blockViolations>0)))throw Error('state/grid failure');
 if(!samples.every(s=>s.cancel?Math.max(...s.rgba.slice(0,3))<100:Math.max(...s.rgba.slice(0,3))>200))throw Error('beam probe failure');
 return {state_and_grid:rows,beam_pixel_probe:samples};
}
