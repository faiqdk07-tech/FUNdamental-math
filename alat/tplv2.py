import re, sys
P='/home/user/FUNdamental-math/index.html'
s=open(P).read()
def tpl_bounds(name):
    a=s.index('<template id="tpl-%s">'%name); b=s.index('</template>',a)+len('</template>'); return a,b

TITLE='''<div class="px-ttl2"><b class="px-f">%s</b><sc-if value="{{gmInPlay}}" hint-placeholder-val="{{ false }}"><span class="px-ttl2-s"><sc-if value="{{v2Hearts}}" hint-placeholder-val="{{ true }}"><span class="px-hearts" aria-label="Kesempatan"><sc-for list="{{v2HeartList}}" as="h" hint-placeholder-count="2"><i class="px-heart {{h}}"></i></sc-for></span></sc-if><span>{{v2StatusTxt}}</span></span></sc-if></div>'''
PICK='''<div class="px-qboard"><div class="px-qboard-h">{{gmPickTitle}}</div>
<sc-for list="{{v2Pick}}" as="pk" hint-placeholder-count="3"><button type="button" onClick="{{pk.tap}}" class="px-qnote {{pk.cls}}"><span class="px-lvdot">{{pk.num}}</span><span class="px-qnote-t"><b>{{pk.name}}</b><small>{{v2LvlName}}</small></span><img alt="" class="px-qnote-ic" src="{{v2GameIc}}"><span class="px-qstamp">Selesai</span></button></sc-for></div>'''
TALK='''<sc-if value="{{hasStory}}" hint-placeholder-val="{{ true }}"><div class="px-talk"><div class="px-talk-who"><span class="px-talk-face"><img alt="" src="{{v2Face}}"></span><span class="px-talk-name px-f">{{v2Name}}</span></div><div class="px-talk-bubble"><sc-if value="{{pxHasTag}}" hint-placeholder-val="{{ true }}"><span class="px-talk-tag px-f">{{gmTagLine}}</span></sc-if>
<div class="px-talk-text">{{story}}</div>
<sc-if value="{{v2NeedTap}}" hint-placeholder-val="{{ true }}"><button type="button" class="px-talk-next px-f" onClick="{{v2Lanjut}}">Lanjut</button></sc-if>
<sc-if value="{{isTut}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 8px; align-items: center; margin-top: 4px"><sc-if value="{{hasTutBtn}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{tutTap}}" class="px-cta px-f">{{tutBtn}}</button></sc-if><button type="button" onClick="{{skipTut}}" class="px-linkbtn">Lewati</button></div></sc-if></div></div>
<sc-if value="{{hasGoal}}" hint-placeholder-val="{{ true }}"><sc-if value="{{v2ShowTask}}" hint-placeholder-val="{{ true }}"><div class="px-task"><span class="px-task-h px-f"><img alt="" src="{{px.misi}}">Tugas</span><div class="px-task-t">{{goal}}</div></div></sc-if></sc-if></sc-if>'''
POP='''<sc-if value="{{v2Msg}}" hint-placeholder-val="{{ false }}"><div class="px-pop {{v2MsgOk}}"><div class="px-pop-card"><div class="px-pop-rib"><i></i><b>{{v2MsgTitle}}</b><i></i></div><div class="px-pop-main"><span class="px-pop-fw"><img alt="" class="px-pop-face" src="{{v2Face}}"></span><div class="px-pop-body"><span class="px-pop-who">{{v2Name}}</span><div>{{msg}}</div></div></div>
<div class="px-pop-act"><button type="button" class="px-btn2 px-f" onClick="{{v2CloseMsg}}">Oke</button><sc-if value="{{gmHasNext}}" hint-placeholder-val="{{ false }}"><button type="button" class="px-cta px-f" onClick="{{gmNext}}">{{gmNextLabel}} ▸</button></sc-if></div></div></div></sc-if>'''
NEXT='''<sc-if value="{{gmHasNext}}" hint-placeholder-val="{{ false }}"><button type="button" onClick="{{gmNext}}" class="px-cta px-f px-next2">{{gmNextLabel}} ▸</button></sc-if>'''

def common(t, name):
    # root class
    t=t.replace('<div class="px-screen ', '<div class="px-screen px-v2 {{v2Wait}} ',1)
    # header row -> hud2 (first flex row inside wall)
    t=re.sub(r'<div style="display: flex; align-items: center; gap: 6px">', '<div class="px-hud2">', t, count=1)
    t=re.sub(r'<div class="px-fw px-ttl"[^>]*>.*?</div>(?=\s*(<button type="button" onClick="\{\{toggleHelp\}\}"|\n<sc-if value="\{\{gmShowMenu))', TITLE%name, t, count=1, flags=re.S)
    # pick list
    t=re.sub(r'<div class="px-fw px-lab px-f">\{\{gmPickTitle\}\}</div>', '%%PICKHEAD%%', t, count=1)
    t=re.sub(r'<sc-for list="\{\{gmPickItems\}\}" as="pk" hint-placeholder-count="3">\s*<button[^\n]*</button>\s*</sc-for>', '%%PICKLIST%%', t, count=1)
    t=t.replace('%%PICKHEAD%%','').replace('%%PICKLIST%%', PICK)
    # popup at end
    i=t.rindex('</div></template>')
    t=t[:i]+POP+'\n'+t[i:]
    return t

def sub1(t, pat, rep, flags=re.S, must=True):
    t2, n = re.subn(pat, lambda m: rep, t, count=1, flags=flags)
    if must and n != 1: raise SystemExit('NOMATCH: ' + pat[:80])
    return t2

CEKRE=r'<button type="button" onClick="\{\{checkAns\}\}"[^>]*>Cek</button>'
CEK='<button type="button" onClick="{{checkAns}}" class="px-cta px-f px-cek">✓ Cek</button>'

def meja(t):
    t=common(t,'Meja Hajatan')
    t=sub1(t, r'<sc-if value="\{\{hasStory\}\}"[^\n]*<div class="px-npc">.*?</div></div></sc-if>', TALK)
    t=sub1(t, r'<sc-if value="\{\{hasMsg\}\}"[^\n]*?<div class="px-msg"[^\n]*?</sc-if>', '')
    t=sub1(t, r'<sc-if value="\{\{gmHasNext\}\}"[^\n]*?</sc-if>', NEXT)
    t=sub1(t, CEKRE, CEK)
    t=sub1(t, r'<button type="button" onClick="\{\{sayKurang\}\}"[^>]*>', '<button type="button" onClick="{{sayKurang}}" class="px-alt px-f"><i>?</i>')
    t=sub1(t, r'<button type="button" onClick="\{\{sayMustahil\}\}"[^>]*>', '<button type="button" onClick="{{sayMustahil}}" class="px-alt px-f"><i>⊘</i>')
    t=sub1(t, r'<div style="border-top: 1px solid #ECEBE7; padding-top: 6px; display: flex; flex-direction: column; gap: 2px">\s*<div style="font-size: 11px; color: #66655F">Catatan percobaan</div>\s*<div style="display: flex; flex-wrap: wrap; gap: 4px">\s*<sc-for list="\{\{log\}\}" as="l" hint-placeholder-count="3">\s*<span[^>]*>\{\{l\}\}</span>',
        '<div class="px-log2"><div class="px-log2-h px-f">Catatan percobaan</div>\n<div class="px-log2-l">\n<sc-for list="{{log}}" as="l" hint-placeholder-count="3">\n<span>{{l}}</span>')
    t=sub1(t, r'<div style="font-size: 12px; color: #66655F">Catatan untuk Pak Harun \(\{\{ruleCount\}\}\)</div>', '<div class="px-rulehead px-f">Catatan untuk Pak Harun ({{ruleCount}})</div>')
    return t

def kasir(t):
    t=common(t,'Kasir Kilat')
    t=sub1(t, r'<sc-if value="\{\{hasStory\}\}" hint-placeholder-val="\{\{ true \}\}">\s*<div class="px-fw px-card">.*?</div>\s*</sc-if>\s*</div>\s*</sc-if>', TALK)
    t=sub1(t, r'<sc-if value="\{\{pxMsgWall\}\}"[^\n]*?</sc-if>', '')
    t=sub1(t, r'<sc-if value="\{\{pxMsgBoard\}\}"[^\n]*?</sc-if>', '')
    t=sub1(t, r'<sc-if value="\{\{gmHasNext\}\}" hint-placeholder-val="\{\{ false \}\}">\s*<button[^\n]*</button>\s*</sc-if>', NEXT)
    t=sub1(t, CEKRE, CEK)
    t=sub1(t, r'<button type="button" onClick="\{\{sayNotEnough\}\}" class="px-fo px-f"[^>]*>', '<button type="button" onClick="{{sayNotEnough}}" class="px-alt px-f"><i>?</i>')
    t=sub1(t, r'<button type="button" onClick="\{\{sayImpossible\}\}" class="px-fo px-f"[^>]*>', '<button type="button" onClick="{{sayImpossible}}" class="px-alt px-f"><i>⊘</i>')
    t=sub1(t, r'<sc-for list="\{\{builders\}\}" as="b" hint-placeholder-count="1">.*?</sc-for>\s*<div class="px-fw px-f"[^>]*>Buku catatan kasir \(\{\{ruleCount\}\}\)</div>\s*<sc-for list="\{\{rules\}\}" as="r" hint-placeholder-count="1">\s*<div class="px-fw"[^>]*>\{\{r\}\}</div>\s*</sc-for>',
        """<sc-for list="{{builders}}" as="b" hint-placeholder-count="1">
<div class="px-rulecard"><div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap">
<span style="font-family: ui-monospace, Menlo, monospace; font-size: 15px">{{b.lhs}} =</span>
<button type="button" onClick="{{b.cyc}}" class="px-chalk2">{{b.rhs}}</button>
<button type="button" onClick="{{b.test}}" class="px-cta px-f" style="margin-left: auto">Uji</button>
</div></div>
</sc-for>
<div class="px-rulehead px-f">Buku catatan kasir ({{ruleCount}})</div>
<sc-for list="{{rules}}" as="r" hint-placeholder-count="1">
<div class="px-rulenote">{{r}}</div>
</sc-for>""")
    return t

for name, fn in [('MejaHajatan', meja), ('KasirKilat', kasir)]:
    a,b=tpl_bounds(name); s=s[:a]+fn(s[a:b])+s[b:]
open(P,'w').write(s)
print('done')
