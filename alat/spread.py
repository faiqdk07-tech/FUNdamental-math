import re
exec(open('/tmp/claude-0/-home-user-FUNdamental-math/aa74a823-bbf9-5dbe-810d-6b8dcb711f71/scratchpad/tplv2.py').read().split("for name, fn in")[0])
NAMES={'ArgoOjek':('yanto','Pak Yanto'),'BagiPizza':('ketua','Ketua Panitia'),'CetakSpanduk':('desainer','Perancang'),'DapurRoti':('mira','Bu Mira'),'DuaStruk':('sari','Bu Sari'),
'GrafikViral':('rara','Mbak Rara'),'GudangKardus':('ratna','Bu Ratna'),'JadwalBus':('kepala','Kepala Terminal'),'KebunPagar':('wati','Bu Wati'),'LipatKertas':('cetak','Kepala Percetakan'),
'LokerOSIS':('wina','Bu Wina'),'MartabakTopping':('udin','Bang Udin'),'MesinMinuman':('rina','Bu Rina'),'PasangLantai':('darto','Pak Darto'),'Pelabuhan':('syahbandar','Syahbandar'),
'PentasSeni':('dimas','Kak Dimas'),'RacikResep':('barista','Barista'),'RaporKelas':('sinta','Bu Sinta'),'RekapGrosir':('lina','Bu Lina'),'RuteKurir':('kurir','Kurir'),
'TanggaBangunan':('mandor','Mandor Joko'),'Timbangan':('mandor','Mandor'),'Ubin':('darto','Pak Darto'),'UndianDoorprize':('pakrt','Pak RT')}
ICON={'?':'?','x':'⊘'}
report=[]
for g,(face,who) in NAMES.items():
  try:
    a,b=tpl_bounds(g); t=s[a:b]
    t0=t
    title=re.search(r'<div class="px-fw px-ttl"[^>]*><b class="px-f">([^<]+)</b>',t).group(1)
    t=common(t,title)
    t=sub1(t, r'<sc-if value="\{\{hasStory\}\}"[^\n]*<div class="px-npc">.*?</div></div></sc-if>', TALK)
    t=sub1(t, r'<sc-if value="\{\{hasMsg\}\}"[^\n]*?<div class="px-msg"[^\n]*?</sc-if>', '')
    t=sub1(t, r'<sc-if value="\{\{gmHasNext\}\}"[^\n]*?</sc-if>', NEXT)
    if '{{checkAns}}' in t:
        t,n=re.subn(r'<button type="button" onClick="\{\{checkAns\}\}"[^>]*>Cek</button>', CEK, t)
        if not n: report.append(g+': cek?')
    for fn,ic in [('sayKurang','?'),('sayNotEnough','?'),('sayMustahil','⊘'),('sayImpossible','⊘')]:
        t,n=re.subn(r'<button type="button" onClick="\{\{%s\}\}"[^>]*>'%fn, '<button type="button" onClick="{{%s}}" class="px-alt px-f"><i>%s</i>'%(fn,ic), t)
    s=s[:a]+t+s[b:]
    # renderVals hook
    ga=s.index('GAMES["%s"]'%g); seg_end=s.index('return Component;',ga)
    seg=s[ga:seg_end]
    m=re.search(r'(renderVals\(\) \{[^\n]*?)(\}\); \})', seg)
    extra=", PX.v2(this, v, { face: '%s', name: '%s', game: '%s' })"%(face,who,title)
    if 'const v =' not in m.group(1):
        newl="renderVals() { const v = PX.modeIcons(this.gmWrap(this.gmRender())); return Object.assign(v, { px: PX.U, pxStage: PX.stage(), pxHasTag: !!v.gmTagLine }"+extra+"); }"
        seg=seg[:m.start()]+newl+seg[m.end():]
    else:
        seg=seg[:m.start()]+m.group(1)+'}'+extra+'); }'+seg[m.end():]
    s=s[:ga]+seg+s[seg_end:]
  except SystemExit as e:
    report.append(g+' LEWATI: '+str(e)[:60])
open(P,'w').write(s)
print('report',report)
