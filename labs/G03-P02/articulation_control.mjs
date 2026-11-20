// Original procedural sanity check; independent of all commercial editors.
function articulationControl(){
 const W=32,K=4,angles=[0,15,30,45,60,75,90];
 const rot=(x,y,a)=>[Math.cos(a)*x-Math.sin(a)*y,Math.sin(a)*x+Math.cos(a)*y];
 const same=(a,b)=>a.length===b.length&&a.every((v,i)=>v===b[i]);
 function pose(deg){
  const a=deg*Math.PI/180,b=a,root=[12,12],v=rot(8,0,a),joint=[root[0]+v[0],root[1]+v[1]];
  const parts=[{origin:root,angle:a,rect:[-1,-2,9,2],color:1},{origin:joint,angle:b,rect:[-1,-1,7,1],color:2}];
  function sample(x,y){
   let c=0;
   for(const p of parts){const [u,v]=rot(x-p.origin[0],y-p.origin[1],-p.angle);const [l,t,r,b]=p.rect;if(u>=l&&u<r&&v>=t&&v<b)c=p.color;}
   return c;
  }
  function render(n){return Array.from({length:n*n},(_,i)=>sample((i%n+.5)*W/n,(Math.floor(i/n)+.5)*W/n));}
  const lo=render(W),hi=render(W*K),up=Array.from({length:(W*K)**2},(_,i)=>lo[Math.floor(Math.floor(i/(W*K))/K)*W+Math.floor((i%(W*K))/K)]);
  function mixed(data){let count=0;for(let y=0;y<W;y++)for(let x=0;x<W;x++){const v=data[y*K*W*K+x*K];let diff=false;for(let j=0;j<K;j++)for(let i=0;i<K;i++)if(data[(y*K+j)*W*K+x*K+i]!==v)diff=true;if(diff)count++;}return count;}
  return {angle:deg,direct_mixed_blocks:mixed(hi),logical_mixed_blocks:mixed(up),output_pixels_different:hi.filter((v,i)=>v!==up[i]).length,identical:same(hi,up),independent_joint_rounding_px:Number(Math.hypot(Math.round(joint[0])-joint[0],Math.round(joint[1])-joint[1]).toFixed(6)),endpoints_coincident:Math.hypot(joint[0]-parts[1].origin[0],joint[1]-parts[1].origin[1])<1e-12,priority_at_overlap:sample(joint[0],joint[1])===2,low_color_count:new Set(lo).size,high_color_count:new Set(hi).size};
 }
 const rows=angles.map(pose);
 const checks={logical_grid_all_poses:rows.every(r=>r.logical_mixed_blocks===0),axis_aligned_control:rows.filter(r=>r.angle===0||r.angle===90).every(r=>r.identical),direct_off_axis_grid_violations:rows.filter(r=>r.angle%90!==0).every(r=>r.direct_mixed_blocks>0),hierarchy_registration:rows.every(r=>r.endpoints_coincident),draw_priority:rows.every(r=>r.priority_at_overlap),palette_preserved:rows.every(r=>r.low_color_count===3&&r.high_color_count===3),isolated_rounding_nonzero:rows.some(r=>r.independent_joint_rounding_px>0)};
 if(!Object.values(checks).every(Boolean))throw new Error(JSON.stringify({rows,checks}));
 return {logical_canvas:[W,W],output_canvas:[W*K,W*K],integer_scale:K,rows,checks};
}
console.log(JSON.stringify(articulationControl(),null,2));
