// Original abstract exposure schedule control.
function timingControl(){
 const radii=[0,2,4,6,8,10,12];
 const variants=[{id:"impulse_then_settle",holds:[1,1,1,2,3,5,11]},{id:"wait_then_release",holds:[11,5,3,2,1,1,1]},{id:"uniform_control",holds:[3,4,3,4,3,4,3]}];
 const rows=variants.map(v=>{const track=radii.flatMap((r,i)=>Array(v.holds[i]).fill(r));return {id:v.id,holds:v.holds,radii_by_tick:track,duration_ticks:track.length,unique_poses:new Set(track).size,first_radius_10_tick:track.findIndex(r=>r>=10),first_radius_12_tick:track.findIndex(r=>r>=12),mean_radius:track.reduce((a,b)=>a+b,0)/track.length,pose_transitions:track.slice(1).filter((x,i)=>x!==track[i]).length};});
 const sampling=rows.map(r=>{const presentations=Array.from({length:60},(_,i)=>r.radii_by_tick[Math.floor(i*24/60)]);const counts=radii.map(x=>presentations.filter(y=>y===x).length);return {id:r.id,presentation_counts:counts,all_poses_seen:counts.every(x=>x>0),total_frames:presentations.length};});
 const checks={equal_total_duration:rows.every(r=>r.duration_ticks===24),same_pose_library:rows.every(r=>r.unique_poses===7&&r.pose_transitions===6),equal_endpoints:rows.every(r=>r.radii_by_tick[0]===0&&r.radii_by_tick[23]===12),distinct_arrival:rows[0].first_radius_10_tick<rows[2].first_radius_10_tick&&rows[2].first_radius_10_tick<rows[1].first_radius_10_tick,same_render_duration:sampling.every(r=>r.total_frames===60),no_pose_skipped_at_60:sampling.every(r=>r.all_poses_seen)};
 if(!Object.values(checks).every(Boolean))throw Error(JSON.stringify(checks));return {authoring_hz:24,output_hz:60,radii,rows,sampling,checks};
}
console.log(JSON.stringify(timingControl(),null,2));
