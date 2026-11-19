import re
exec(open('/tmp/claude-0/-home-user-FUNdamental-math/aa74a823-bbf9-5dbe-810d-6b8dcb711f71/scratchpad/tplv2.py').read().split("for name, fn in")[0])

# PX.v2: allow story/goal/hasGoal from options, and hearts from gmStatusLine
old = "const m = String(v.status || '').match(/(\\d+)\\s*\\/\\s*(\\d+)/), useH = !!m && /kesempatan/i.test(String(v.statusLabel || ''));"
assert old in s, 'v2 hearts'
s = s.replace(old, "const stTxt = v.statusLabel ? String(v.status || '') : String(v.gmStatusLine || ''), stLab = v.statusLabel ? String(v.statusLabel) : String(v.gmStatusLine || ''); const m = stTxt.match(/(\\d+)\\s*\\/\\s*(\\d+)/), useH = !!m && /kesempatan/i.test(stLab);", 1)
old = "const key = String(v.story || '') + '|' + String(v.goal || '');"
assert old in s, 'v2 key'
s = s.replace(old, "const story = o.story !== undefined ? o.story : v.story, goal = o.goal !== undefined ? o.goal : v.goal, hasGoal = o.hasGoal !== undefined ? o.hasGoal : v.hasGoal; const key = String(story || '') + '|' + String(goal || '');", 1)
old = "const needTap = !!v.hasGoal && !v.isTut;"
assert old in s, 'v2 needTap'
s = s.replace(old, "const needTap = !!hasGoal && !v.isTut;", 1)
old = "v2StatusTxt: useH ? '' : (/^status$/i.test(String(v.statusLabel || '')) ? String(v.status || '') : [v.statusLabel, v.status].filter(Boolean).join(' · ')),"
assert old in s, 'v2 status'
s = s.replace(old, "v2StatusTxt: useH ? '' : (v.statusLabel ? (/^status$/i.test(String(v.statusLabel)) ? String(v.status || '') : [v.statusLabel, v.status].filter(Boolean).join(' · ')) : String(v.gmStatusLine || '')),", 1)

WHO = '<div class="px-talk-who"><span class="px-talk-face"><img alt="" src="{{v2Face}}"></span><span class="px-talk-name px-f">{{v2Name}}</span></div>'
LANJUT = '<sc-if value="{{v2NeedTap}}" hint-placeholder-val="{{ true }}"><button type="button" class="px-talk-next px-f" onClick="{{v2Lanjut}}">Lanjut</button></sc-if>'
GOAL = '''<sc-if value="{{isGoal}}" hint-placeholder-val="{{ true }}"><div class="px-talk">%s<div class="px-talk-bubble"><div class="px-talk-text">{{misiStory}}</div><div class="px-legend"><img alt="" src="{{px.kardus}}" width="15" height="14">? = satu kardus</div>%s</div></div>
<sc-if value="{{v2ShowTask}}" hint-placeholder-val="{{ true }}"><div class="px-task"><span class="px-task-h px-f"><img alt="" src="{{px.misi}}">Tugas</span><div class="px-task-t">{{misiGoal}}</div></div></sc-if></sc-if>''' % (WHO, LANJUT)
TUT = '''<sc-if value="{{isTut}}" hint-placeholder-val="{{ false }}"><div class="px-talk">%s<div class="px-talk-bubble"><span class="px-talk-tag px-f">{{tutStep}}</span><div class="px-talk-text">{{tutText}}</div>
<div style="display: flex; gap: 8px; align-items: center; margin-top: 4px"><sc-if value="{{hasTutBtn}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{tutTap}}" class="px-cta px-f">{{tutBtn}}</button></sc-if><button type="button" onClick="{{skipTut}}" class="px-linkbtn">Lewati latihan</button></div></div></div></sc-if>''' % WHO
HARIAN = '''<sc-if value="{{isHarian}}" hint-placeholder-val="{{ false }}"><div class="px-talk">%s<div class="px-talk-bubble"><span class="px-talk-tag px-f">{{hCase.konteks}}</span><div style="display: flex; gap: 4px; flex-wrap: wrap"><sc-for list="{{hCase.tags}}" as="g" hint-placeholder-count="1"><span class="px-tag px-f" style="background: #FFC58A">{{g}}</span></sc-for></div>
<div class="px-talk-text">{{hCase.cerita}}</div><div class="px-legend">{{hCase.legend}}</div>%s</div></div>
<sc-if value="{{v2ShowTask}}" hint-placeholder-val="{{ true }}"><div class="px-task"><span class="px-task-h px-f"><img alt="" src="{{px.misi}}">Tugas</span><div class="px-task-t">{{hCase.tujuan}}</div></div></sc-if></sc-if>''' % (WHO, LANJUT)

a, b = tpl_bounds('Timbangan'); t = s[a:b]
t = common(t, 'Timbangan')
t = sub1(t, r'<sc-if value="\{\{isGoal\}\}"[^\n]*<div class="px-npc">.*?</div></div></sc-if>', GOAL)
t = sub1(t, r'<sc-if value="\{\{isTut\}\}"[^\n]*<div class="px-npc">.*?</div></div></div></sc-if>', TUT)
t = sub1(t, r'<sc-if value="\{\{isHarian\}\}"[^\n]*<div class="px-npc">.*?</div></div></sc-if>', HARIAN)
t = sub1(t, r'<sc-if value="\{\{hasMsg\}\}"[^\n]*?<div class="px-msg"[^\n]*?</sc-if>', '')
t = sub1(t, r'<sc-if value="\{\{gmHasNext\}\}"[^\n]*?</sc-if>', NEXT)
for fn, ic in [('sayNotEnough', '?'), ('sayImpossible', '⊘')]:
    t, n = re.subn(r'<button type="button" onClick="\{\{%s\}\}"[^>]*>' % fn, '<button type="button" onClick="{{%s}}" class="px-alt px-f"><i>%s</i>' % (fn, ic), t)
s = s[:a] + t + s[b:]

old = "renderVals() { return Object.assign(PX.modeIcons(this.gmWrap(this.gmRender())), { px: PX.U, pxStage: PX.stage() }); }"
assert old in s, 'timb render'
s = s.replace(old, "renderVals() { const v = PX.modeIcons(this.gmWrap(this.gmRender())); const hc = v.hCase || {}; return Object.assign(v, { px: PX.U, pxStage: PX.stage() }, PX.v2(this, v, { face: 'mandor', name: 'Mandor', game: 'Timbangan', story: v.isHarian ? hc.cerita : v.misiStory, goal: v.isHarian ? hc.tujuan : v.misiGoal, hasGoal: !!(v.isGoal || v.isHarian) })); }", 1)
open(P, 'w').write(s)
print('ok')
