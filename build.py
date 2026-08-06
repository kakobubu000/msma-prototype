#!/usr/bin/env python3
"""
Builds index.html for the MSMA prototype.

Language policy: all user-facing wording comes from Halle's MSMA
documentation and the GCS Mentee Decision Tree crosswalk. Recommended
Training/Skills descriptions live in skills.json and were written by
Halle. Anything the crosswalk recommends but skills.json does not cover
renders as a visible placeholder rather than substitute text.

Delivery model (per 7/28 meeting): the MSMA is completed by one member
of the student's school team, after the Top Needs Assessment interviews
are finished.

To edit the skill descriptions, edit skills.json and re-run this file.
"""

import json

MARK = open("logo_mark.txt").read().strip()
WORD = open("logo_word.txt").read().strip()

TRAININGS = json.load(open("skills.json"))
TRAININGS.pop("_comment", None)

# Crosswalk wording that differs from the skills.json key for the same skill.
ALIASES = {
    "Executive Function Skills": "Executive Functioning Skills",
    "Communication": "Communication Skills",
}

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mentee Skill Matching Assessment (MSMA)</title>
<style>
  :root{
    --ink:#1f2a28; --muted:#5f6f6b; --faint:#8aa09a;
    --teal:#0f6e56; --teal-mid:#1d9e75; --teal-soft:#e1f5ee;
    --amber:#b97515; --amber-soft:#faeeda;
    --line:#dce6e3; --card:#ffffff; --bg:#f6faf8;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; background:var(--bg); color:var(--ink); line-height:1.6;}
  .wrap{max-width:780px; margin:0 auto; padding:40px 20px 60px;}
  .brand{display:flex; align-items:center; justify-content:center; gap:13px; margin-bottom:16px;}
  .brand-mark{height:50px; width:auto;}
  .brand-word{height:31px; width:auto;}
  @media(max-width:480px){.brand-mark{height:42px;} .brand-word{height:26px;}}
  h1{font-size:25px; font-weight:600; text-align:center;}
  .sub{text-align:center; color:var(--muted); font-size:15px; margin-top:8px;}
  .center{text-align:center;}
  .card{background:var(--card); border:1px solid var(--line); border-radius:14px; padding:26px 28px; margin-top:24px;}
  .btn{display:inline-block; font-size:15px; font-weight:500; color:#fff; background:var(--teal); border:none; border-radius:10px; padding:12px 26px; cursor:pointer; margin-top:18px;}
  .btn.ghost{background:transparent; color:var(--teal); border:1px solid var(--line);}
  .btn:hover{opacity:.92;} .btn:disabled{opacity:.4; cursor:not-allowed;}
  .opt{display:block; width:100%; text-align:left; font-size:15px; background:#fff; border:1px solid var(--line); border-radius:10px; padding:13px 16px; margin-top:10px; cursor:pointer; color:var(--ink);}
  .opt:hover{border-color:var(--teal-mid); background:var(--teal-soft);}
  .back{background:none; border:none; color:var(--faint); font-size:13px; cursor:pointer; margin-top:14px;}
  .domain{font-size:12px; color:var(--teal); text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;}
  .q{font-size:17px; font-weight:500; line-height:1.5;}
  .chip{font-size:12px; padding:2px 10px; border-radius:999px; display:inline-block;}
  .chip.high{background:var(--teal-soft); color:var(--teal);}
  .chip.partial{background:#eaf3de; color:#3b6d11;}
  .chip.low{background:var(--amber-soft); color:var(--amber);}
  .skillcard{background:var(--bg); border-radius:10px; padding:15px 17px; margin-top:10px;}
  .skillcard h4{font-size:14px; margin-bottom:6px; color:var(--teal);}
  .skillcard p{color:var(--muted); font-size:13.5px; line-height:1.55;}
  .skillcard .res{margin-top:8px; font-size:12.5px; color:var(--faint);}
  .skillcard .res b{color:var(--muted); font-weight:500;}
  .placeholder{border:1px dashed var(--line); background:transparent; border-radius:10px; padding:15px 17px; margin-top:10px; font-size:13.5px; color:var(--faint); line-height:1.55;}
  .placeholder h4{font-size:14px; margin-bottom:6px; color:var(--faint);}
  .note{font-size:12.5px; color:var(--faint); margin-top:16px; line-height:1.5;}
  .compass{font-size:13.5px; background:var(--teal-soft); color:var(--teal); border-radius:10px; padding:12px 16px; margin-top:16px;}
  .refer{font-size:13px; background:var(--amber-soft); color:#7a4d0c; border-radius:10px; padding:12px 16px; margin-top:14px; line-height:1.5;}
  .subhead{font-size:13px; color:var(--muted); margin-top:18px; font-weight:500;}
  table{width:100%; border-collapse:collapse; font-size:13px; margin-top:12px;}
  th{font-weight:500; color:var(--muted); text-align:left; padding:8px 6px; border-bottom:1px solid var(--line); font-size:12px;}
  td{padding:9px 6px; border-bottom:1px solid var(--line); vertical-align:top;}
  .hidden{display:none;}
  h2{font-size:19px; font-weight:600;}
  h3{font-size:15px; font-weight:600; margin-top:22px;}
  .field{display:block; width:100%; font-size:14px; border:1px solid var(--line); border-radius:8px; padding:10px 12px; margin-top:6px; background:#fff; color:var(--ink); font-family:inherit;}
  .lbl{font-size:12.5px; color:var(--muted); margin-top:14px; display:block;}
  .two{display:grid; grid-template-columns:1fr 1fr; gap:14px;}
  .needs{margin-top:16px;}
  .needrow{display:grid; grid-template-columns:110px 1fr 1fr 1fr; gap:10px; align-items:center; margin-top:10px;}
  .needhead{display:grid; grid-template-columns:110px 1fr 1fr 1fr; gap:10px; font-size:12px; color:var(--muted); margin-top:18px;}
  .needrow .who{font-size:14px; font-weight:500;}
  @media(max-width:660px){
    .two{grid-template-columns:1fr;}
    .needrow{grid-template-columns:1fr; gap:6px; padding-bottom:12px; border-bottom:1px solid var(--line);}
    .needhead{display:none;}
    .needrow .who{margin-top:8px;}
  }
  footer{text-align:center; font-size:12px; color:var(--faint); margin-top:36px; line-height:1.6;}
  @media print{ body{background:#fff;} .no-print{display:none !important;} .card{border:none; padding:6px 0;} }
</style>
</head>
<body>
<div class="wrap">
  <div class="brand">
    <img class="brand-mark" src="__MARK__" alt="">
    <img class="brand-word" src="__WORD__" alt="YESS Lab">
  </div>
  <h1>Mentee Skill Matching Assessment (MSMA)</h1>
  <p class="sub">Integrated School Mentoring &bull; YESS Lab &bull; University of South Carolina</p>

  <div id="screen-start" class="card">
    <p style="color:var(--muted); font-size:15px;">The purpose of the MSMA is to translate a mentee&rsquo;s identified needs into the specific mentoring skills that can become the focus of the mentoring relationship. This assessment is to be completed after the Top Needs Assessment by the school team, counselor, social worker, or mentoring coordinator.</p>
    <div class="center"><button class="btn" onclick="go('entry')">Begin</button></div>
  </div>

  <div id="screen-entry" class="card hidden">
    <p class="domain">Section 1</p>
    <h2>Compile Top Needs</h2>
    <p class="note" style="margin-top:6px;">One team member will input the needs from each respondent after completion of the Top Needs Assessment.</p>
    <div class="two">
      <div>
        <label class="lbl" for="f-role">Completed by (role on the school team)</label>
        <input class="field" id="f-role" placeholder="e.g. school counselor, school psychologist, mentoring coordinator">
      </div>
      <div>
        <label class="lbl" for="f-case">Student ID or case code</label>
        <input class="field" id="f-case" placeholder="e.g. GCS-0417">
      </div>
    </div>
    <div class="needs">
      <p style="font-size:14.5px; margin-top:20px;">&ldquo;Enter the Top Needs identified by each member:&rdquo;</p>
      <div class="needhead"><span></span><span>Need #1</span><span>Need #2</span><span>Need #3</span></div>
      <div class="needrow"><span class="who">Caregiver</span>
        <select class="field" id="care1" onchange="checkReady()"></select>
        <select class="field" id="care2"></select><select class="field" id="care3"></select></div>
      <div class="needrow"><span class="who">Teacher</span>
        <select class="field" id="teach1" onchange="checkReady()"></select>
        <select class="field" id="teach2"></select><select class="field" id="teach3"></select></div>
      <div class="needrow"><span class="who">Mentee</span>
        <select class="field" id="ment1" onchange="checkReady()"></select>
        <select class="field" id="ment2"></select><select class="field" id="ment3"></select></div>
    </div>
    <div class="center"><button class="btn" id="entry-btn" onclick="runMatch()" disabled>Determine Primary Underlying Skill</button></div>
    <button class="back no-print" onclick="go('start')">&#8592; Back</button>
  </div>

  <div id="screen-dq" class="card hidden">
    <p class="domain">Section 3</p>
    <h2>Decision Questions</h2>
    <p style="margin-top:8px; color:var(--muted); font-size:14px;">These questions are answered if all three members differ in their Top Need.</p>
    <div id="dq-list" class="note" style="margin-top:10px;"></div>
    <div id="dq-body" style="margin-top:18px;"></div>
    <button class="back no-print" onclick="restartDQ()">&#8592; Start Decision Questions over</button>
  </div>

  <div id="screen-results" class="card hidden">
    <p class="domain">The Results</p>
    <h2>Section 3: Determine the Primary Underlying Skill</h2>
    <p style="color:var(--muted); font-size:14px; margin-top:6px;">Skill Convergence: The MSMA compares the identified concerns against the mentoring skill crosswalk to determine whether different concerns reflect the same underlying developmental skill needs.</p>
    <div class="compass" id="conv-box"></div>
    <div id="refer-box"></div>

    <h3>Section 2: Identify Patterns</h3>
    <p style="font-size:13.5px; color:var(--muted); margin-top:4px;" id="pattern-line"></p>

    <h3>Section 4: Needs Convergence Matrix</h3>
    <table id="matrix"></table>
    <p class="note">Columns auto-populate the needs, skill, and recommendation. Priority is populated as High, Partial, or Low depending on the Skill convergence.</p>

    <h3>Section 5: Summary</h3>
    <div id="summary"></div>

    <div class="center no-print">
      <button class="btn ghost" onclick="copyResults(this)">Copy results</button>
      <button class="btn ghost" onclick="window.print()">Save (PDF)</button>
    </div>
    <div class="center no-print">
      <button class="btn ghost" onclick="go('entry')">&#8592; Back to Section 1</button>
      <button class="btn ghost" onclick="location.reload()">New assessment</button>
    </div>
  </div>

  <footer>MSMA draft prototype, in development with the YESS Lab mentoring team.<br>Concern list, skill crosswalk, and skill descriptions from the MSMA documentation and the GCS Mentee Decision Tree.</footer>
</div>

<script>
const SKILLS = {
  ef:   "Executive Functioning / Time management",
  acad: "Learning strategies / Study habits",
  goal: "Goal setting, self-efficacy",
  emot: "Emotion Regulation",
  well: "Emotional wellness",
  conf: "Confidence Building",
  comm: "Communication and empathy",
  cres: "Conflict resolution"
};

/* Recommended Training/Skills descriptions, written by Halle (skills.json) */
const TRAININGS = __TRAININGS__;
/* Crosswalk wording that differs from the skills.json key for the same skill */
const ALIASES = __ALIASES__;

const CONCERNS = [
  {label:"Incomplete work",            domain:"Academic",   skill:"ef",   need:"Task initiation, planning, time management", res:"Time Management, Task Planning, Goal Setting"},
  {label:"Grade dropping",             domain:"Academic",   skill:"acad", need:"Study habits, academic engagement",          res:"Study Skills, Academic Success Strategies, Growth Mindset"},
  {label:"Poor study habits",          domain:"Academic",   skill:"acad", need:"Learning strategies",                        res:"Study Skills, Note Taking, Test Preparation"},
  {label:"Missing assignments",        domain:"Academic",   skill:"ef",   need:"Organization, accountability",               res:"Organization, Planner Systems, Time Management"},
  {label:"Low academic motivation",    domain:"Academic",   skill:"goal", need:"Goal setting, self-efficacy",                res:"Goal Setting, Motivation, Growth Mindset"},
  {label:"Organization",               domain:"Behavioral", skill:"ef",   need:"Executive functioning",                      res:"Organization Systems, Executive Function Skills"},
  {label:"Procrastination",            domain:"Behavioral", skill:"ef",   need:"Task initiation, prioritization",            res:"Prioritization, Time Blocking, Breaking Tasks into Steps"},
  {label:"Poor time management",       domain:"Behavioral", skill:"ef",   need:"Planning and scheduling",                    res:"Time Management, Routine Building"},
  {label:"Poor attendance",            domain:"Behavioral", skill:"goal", need:"Habits, accountability",                     res:"Habit Building, Accountability, Goal Setting"},
  {label:"Difficulty staying focused", domain:"Behavioral", skill:"ef",   need:"Attention and self-management",              res:"Self-Regulation, Focus Strategies, Executive Function Skills"},
  {label:"Stress",                     domain:"Emotional",  skill:"emot", need:"Coping strategies",                          res:"Stress Management, Mindfulness, Relaxation Techniques"},
  {label:"Anxiety",                    domain:"Emotional",  skill:"emot", need:"Emotional regulation",                       res:"Coping Skills, Emotional Regulation, Mindfulness"},
  {label:"Sadness/Depression",         domain:"Emotional",  skill:"well", need:"Emotional wellness",                         res:"Emotional Wellness, Resilience, Self-Care", refer:true},
  {label:"Low self-confidence",        domain:"Emotional",  skill:"conf", need:"Self-efficacy",                              res:"Confidence Building, Strengths-Based Coaching, Positive Self-Talk"},
  {label:"Feeling overwhelmed",        domain:"Emotional",  skill:"emot", need:"Prioritization and coping",                  res:"Stress Management, Organization, Resilience"},
  {label:"Relationship struggles",     domain:"Social",     skill:"comm", need:"Communication and empathy",                  res:"Communication Skills, Healthy Relationships, Emotional Intelligence"},
  {label:"Conflict with peers",        domain:"Social",     skill:"cres", need:"Conflict resolution",                        res:"Conflict Resolution, Active Listening, Problem Solving"},
  {label:"Difficulty making friends",  domain:"Social",     skill:"comm", need:"Social skills",                              res:"Relationship Building, Social Skills, Communication"},
  {label:"Poor communication",         domain:"Social",     skill:"comm", need:"Interpersonal effectiveness",                res:"Communication Skills, Active Listening, Assertiveness"}
];

const DOMAIN_ORDER = ["Social","Emotional","Behavioral","Academic"];
const SOURCES = [{key:"care", label:"Caregiver"},{key:"teach", label:"Teacher"},{key:"ment", label:"Mentee"}];
const PATTERNS = {
  High:    "All three members identified essentially the same primary concern",
  Partial: "Two sources agreed on the primary concern",
  Low:     "All three sources identified different concerns"
};

let state = {};
function concernBy(l){ return CONCERNS.find(c => c.label === l); }
function trainingFor(name){ return TRAININGS[name] || TRAININGS[ALIASES[name]] || null; }

function fillSelects(){
  SOURCES.forEach(s => [1,2,3].forEach(n => {
    const sel = document.getElementById(s.key + n);
    sel.innerHTML = "";
    const blank = document.createElement("option");
    blank.value = ""; blank.textContent = n === 1 ? "Select Need #1..." : "Optional...";
    sel.appendChild(blank);
    DOMAIN_ORDER.forEach(d => {
      const g = document.createElement("optgroup"); g.label = d;
      CONCERNS.filter(c => c.domain === d).forEach(c => {
        const o = document.createElement("option");
        o.value = c.label; o.textContent = c.label; g.appendChild(o);
      });
      sel.appendChild(g);
    });
  }));
}
fillSelects();

function checkReady(){
  document.getElementById("entry-btn").disabled =
    !SOURCES.every(s => document.getElementById(s.key + "1").value);
}
function go(name){
  ["start","entry","dq","results"].forEach(s =>
    document.getElementById("screen-" + s).classList.toggle("hidden", s !== name));
  window.scrollTo(0,0);
}

function runMatch(){
  const picks = SOURCES.map(s => ({
    key:s.key, source:s.label,
    primary: concernBy(document.getElementById(s.key + "1").value),
    extras: [2,3].map(n => document.getElementById(s.key + n).value).filter(Boolean)
  }));
  const tally = {};
  picks.forEach(p => tally[p.primary.skill] = (tally[p.primary.skill] || 0) + 1);
  const ranked = Object.entries(tally).sort((a,b) => b[1] - a[1]);
  const top = ranked[0][1];
  state = {picks, dq:{},
    role: document.getElementById("f-role").value.trim(),
    caseId: document.getElementById("f-case").value.trim()};
  if (top === 3){ state.level="High"; state.primarySkill=ranked[0][0]; state.secondarySkill=null; }
  else if (top === 2){ state.level="Partial"; state.primarySkill=ranked[0][0]; state.secondarySkill=ranked[1][0]; }
  else { state.level="Low"; return startDQ(); }
  showResults();
}

function startDQ(){
  state.dq = {}; go("dq");
  document.getElementById("dq-list").innerHTML =
    state.picks.map(p => p.source + " &rarr; " + p.primary.label).join("<br>");
  renderDQ(1);
}
function restartDQ(){ startDQ(); }
function dqOptions(q, list, next){
  const box = document.getElementById("dq-body");
  box.innerHTML = "<p class='q'>" + q + "</p>";
  list.forEach(o => { const b=document.createElement("button"); b.className="opt";
    b.innerHTML=o.text; b.onclick=()=>next(o.value); box.appendChild(b); });
  window.scrollTo(0,0);
}
function sourceOpts(){ return state.picks.map(p => ({value:p.key, text:p.source + " Top Need &mdash; " + p.primary.label})); }
function renderDQ(n){
  if (n===1) dqOptions("1. &ldquo;What concern currently causes the greatest impairment?&rdquo;",
    DOMAIN_ORDER.map(d=>({value:d, text:d+" Functioning"})), v=>{state.dq.impairment=v; renderDQ(2);});
  else if (n===2) dqOptions("2. &ldquo;What concern is most likely to prevent success within mentoring if left unaddressed?&rdquo;",
    sourceOpts(), v=>{state.dq.q2=v; renderDQ(3);});
  else if (n===3) dqOptions("3. &ldquo;Which concern is most developmentally appropriate for mentoring?&rdquo;",
    sourceOpts().concat([{value:"combination", text:"Combination"}]),
    v=>{ state.dq.q3=v; if (v!=="combination" && v===state.dq.q2) resolveDQ([state.dq.q2]); else renderDQ(4); });
  else if (n===4) dqOptions("&ldquo;Do these concerns point to similar underlying needs?&rdquo;",
    [{value:"yes", text:"Yes &mdash; primary focus as both, with overlapping skills"},{value:"no", text:"No"}],
    v=>{ state.dq.similar=v;
      if (v==="yes") resolveDQ(state.dq.q3==="combination" ? state.picks.map(p=>p.key) : [state.dq.q2, state.dq.q3]);
      else renderDQ(5); });
  else if (n===5) dqOptions("&ldquo;Which concern is affecting the student most across settings?&rdquo;",
    sourceOpts(), v=>{ state.dq.across=v; resolveDQ([v]); });
}
function resolveDQ(keys){
  const chosen = keys.map(k => state.picks.find(p => p.key === k));
  state.primarySkill = chosen[0].primary.skill;
  state.secondarySkill = chosen.length > 1 ? chosen[1].primary.skill : null;
  if (state.secondarySkill === state.primarySkill) state.secondarySkill = null;
  showResults();
}

/* ---- Section 5 ---- */
function trainingsFor(skillId){
  const names = [];
  state.picks.filter(p => p.primary.skill === skillId).forEach(p =>
    p.primary.res.split(", ").forEach(t => { if (!names.includes(t)) names.push(t); }));
  return names;
}
function trainingCard(name){
  const t = trainingFor(name);
  if (!t) return "<div class='placeholder'><h4>" + name + "</h4>" +
    "A description for this recommended skill has not been written yet.</div>";
  return "<div class='skillcard'><h4>" + name + "</h4>" +
    "<p><b>What this means for mentoring:</b> " + t.what + "</p>" +
    "<p class='res'><b>Suggested Resources:</b> " + t.resources + "</p></div>";
}

let resultLines = [];
function showResults(){
  go("results");
  const lvl = state.level, cls = lvl.toLowerCase();
  const defn = {
    High:   "The concerns map to the same mentoring skills. Respondents may have identified different concerns, but these concerns map to the same mentoring skill area.",
    Partial:"The concern maps to two related mentoring skills.",
    Low:    "The concerns map to three distinct mentoring skill areas."
  }[lvl];
  const pri = SKILLS[state.primarySkill], sec = state.secondarySkill ? SKILLS[state.secondarySkill] : null;
  const meta = [state.caseId ? "Student " + state.caseId : "", state.role ? "Completed by " + state.role : ""]
    .filter(Boolean).join(" &nbsp;&bull;&nbsp; ");

  document.getElementById("conv-box").innerHTML =
    "<span class='chip " + cls + "'>" + lvl + " Convergence</span><br><span style='color:var(--muted)'>" + defn + "</span><br><br>" +
    (sec ? "<b>Primary Skill:</b> " + pri + "<br><b>Secondary Skill:</b> " + sec : "<b>Underlying Skill:</b> " + pri) +
    (meta ? "<br><br><span style='color:var(--faint); font-size:12.5px;'>" + meta + "</span>" : "");

  document.getElementById("pattern-line").textContent = PATTERNS[lvl];

  const flagged = state.picks.filter(p => p.primary.refer);
  document.getElementById("refer-box").innerHTML = flagged.length
    ? "<div class='refer'>Sadness/Depression identified by " + flagged.map(p=>p.source).join(", ") +
      ". The crosswalk notes referral if indicated.</div>" : "";

  const tbl = document.getElementById("matrix");
  tbl.innerHTML = "<tr><th>Source</th><th>Need Identified</th><th>Underlying Skill</th><th>Priority</th><th>Recommendation</th></tr>";
  state.picks.forEach(p => {
    const extras = p.extras.length
      ? "<br><span style='color:var(--faint); font-size:12px;'>" + p.extras.join(", ") + "</span>" : "";
    tbl.innerHTML += "<tr><td><b>" + p.source + "</b></td><td>" + p.primary.label + extras +
      "</td><td>" + p.primary.need + "</td><td><span class='chip " + cls + "'>" + lvl +
      "</span></td><td>" + p.primary.res + "</td></tr>";
  });

  const priNames = trainingsFor(state.primarySkill);
  const secNames = state.secondarySkill ? trainingsFor(state.secondarySkill) : [];
  let html = "<p class='subhead'>Recommended Training/Skills for " + pri + "</p>" +
             priNames.map(trainingCard).join("");
  if (secNames.length)
    html += "<p class='subhead'>Secondary: " + sec + "</p>" + secNames.map(trainingCard).join("");
  document.getElementById("summary").innerHTML = html;

  resultLines = ["Mentee Skill Matching Assessment (MSMA)"];
  if (state.caseId) resultLines.push("Student " + state.caseId);
  if (state.role)   resultLines.push("Completed by " + state.role);
  resultLines.push("", lvl + " Convergence", defn, "");
  state.picks.forEach(p => resultLines.push("  " + p.source + ": " + p.primary.label + " -> " + p.primary.need));
  resultLines.push("", sec ? "Primary Skill: " + pri + "\nSecondary Skill: " + sec : "Underlying Skill: " + pri, "");
  const line = n => { const t = trainingFor(n);
    return t ? n + "\n  What this means for mentoring: " + t.what + "\n  Suggested Resources: " + t.resources
             : n + "\n  (description not yet written)"; };
  resultLines.push("Recommended Training/Skills:", ...priNames.map(line));
  if (secNames.length) resultLines.push("", "Secondary:", ...secNames.map(line));
  if (flagged.length) resultLines.push("", "Sadness/Depression identified. Crosswalk notes referral if indicated.");
}

function copyResults(btn){ copyText(resultLines.join("\n"), btn); }
function copyText(t, btn){
  const done = () => { const o = btn.textContent; btn.textContent = "Copied"; setTimeout(()=>btn.textContent=o, 1500); };
  if (navigator.clipboard) navigator.clipboard.writeText(t).then(done).catch(()=>fallbackCopy(t,done));
  else fallbackCopy(t, done);
}
function fallbackCopy(text, done){
  const ta=document.createElement("textarea"); ta.value=text; document.body.appendChild(ta); ta.select();
  try{document.execCommand("copy");}catch(e){} document.body.removeChild(ta); done();
}
</script>
</body>
</html>
"""

HTML = (HTML.replace("__MARK__", MARK)
            .replace("__WORD__", WORD)
            .replace("__TRAININGS__", json.dumps(TRAININGS, indent=2))
            .replace("__ALIASES__", json.dumps(ALIASES, indent=2)))
open("index.html", "w", encoding="utf-8").write(HTML)

# coverage report
used = sorted({t.strip() for c in HTML.split('res:"')[1:] for t in c.split('"')[0].split(",")})
missing = [n for n in used if n not in TRAININGS and n not in ALIASES]
print("built index.html (%.0f KB)" % (len(HTML.encode())/1024))
print("skill descriptions: %d   aliased: %d" % (len(TRAININGS), len(ALIASES)))
if missing:
    print("NO DESCRIPTION YET: " + ", ".join(missing))
