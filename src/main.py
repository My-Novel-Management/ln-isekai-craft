#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 10K
#   4. Spec
#   5. Plot         - 1/4: 25K
#   6. Scenes
#   7. Conte        - 1/2: 50K
#   8. Layout
#   9. Draft        - 1/1: 100K
#
################################################################

# Constant
TITLE = "異世界クラフト倶楽部"
MAJOR, MINOR, MICRO = 0, 2, 0
COPY = "異世界をクラフトする"
ONELINE = "クラフトゲームによく似た異世界で、クラフトしながら必死に生き延びる"
OUTLINE = "全１０話予定の異世界ファンタジィ長編。クラフトゲームを思わせる異世界に来てしまった男子は、ゾンビに追いかけられている少年と出会った"
THEME = "すぐに死ぬ可能性のある世界では、生き延びるだけで奇跡だ"
GENRE = "転移ファンタジー"
TARGET = "10-30years"
SIZE = "100K"
CONTEST_INFO = ""
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["転生／転移", "ファンタジー", "男主人公", "ヒューマンドラマ",]
RELEASED = (1, 1, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            w.plot_setup("気づいたら$soutaはクラフトゲームによく似た世界にいた"),
            w.plot_setup("$soutaは$gameというゲームをこよなく愛していた"),
            w.plot_setup("$soutaは$gameではシングルプレイでこつこつ地道に素材集めとモノ造り、建築をするのが好きだった"),
            w.plot_setup(""),# TODO
            w.plot_turnpoint("家の前で倒れていた$nagisaを助けた"),
            w.plot_resolve("リスポーンした$soutaはどこかに転移したと思しき仲間たちを探して、",
                "決意をして拠点を出て、広大な森へと足を踏み入れていった"),
            "※一分で四百から六百文字なので五百文字として三十分で一万五千字程度が目安",
            "１話を４分割すると読みやすいから、結果、五千字を１エピソードに。一話毎に４エピソードで全体で４０から４８ある予定",
            "ゾンビに追われていた$kosukeを助ける$souta",
            "ドアを叩く音が聞こえて、またゾンビかと思ったら、一人の女の子が倒れていた",
            "空腹で死にそうになっていた$nagisaを助ける",
            "彼女も$soutaたちと同じく気づいたらこの世界にいて、ベッドもない中で、恐怖の夜をなんとか乗り越えてここまで逃げてきたという",
            "ベッドで眠ると夢を見ないし、すぐ朝になる",
            "三人でこの世界のルールとゲームの世界との差異について情報交換をする",
            "（ここで一旦世界のルールの確認）",
            "ゲームのようにレシピも見れないので、一度作ったものはメモをしておくことにした",
            "また周囲の地図も手書きでなんとか作り始める",
            "村か何かあれば交易で新しい素材が手に入るというが、その為には周辺の探索を行う必要があった",
            "周辺の探索をする前に、ゲームと同じようにリスポーンするのかどうかが問題となる",
            "しかし自分の命を使ってまでリスポーン試験をする訳にはいかず",
            "あるとき、旅人が拠点にやってくる",
            "その人物は村から近隣の村がないか探してやってきたという",
            "彼もまた$soutaたちと同じく転移人のようだったが、かなり以前にこの世界にやってきたらしい",
            "彼からゲームの世界と似ている部分もあるけれど全然違うことを聞く",
            "また村での生活に馴染んでいるけれど、今までリスポーンを試したことはないと答えた",
            "彼はクラフトゲームが好きすぎて、夢の中でも常にクラフトしているようになり、ある日気づくとこの世界にいたと説明する",
            "彼は村に招待したいと言い出したが、三人は意見が割れてしまい、彼から村の場所だけ聞いて、彼とは別れた",
            "しかし$kosukeが襲われて、目の前から消えてしまい、リスポーンはしなかった",
            "この世界で死ぬことが確定し、怯え始める$nagisa",
            "彼女は村へと助けを求めて拠点を出てしまい、一人残されてしまう$souta",
            "$soutaは一人で生き抜くことを誓い、躊躇していた周辺地域の開拓に乗り出す",
            "一人きりで知らない場所にリスポーンしてしまった$soutaは、仲間たちを探しに再びマイクラフトの旅に出る（ここで続く的に一巻終わり）",
            )


# Notes
def writer_note(w: World):
    return w.writer_note("作者の覚書",
            )


def story_elements(w: World):
    return w.writer_note("作中のマイクラ要素",
            "ゾンビに追いかけられる",
            "高いところから落ちる",
            "マグマダイブ",
            "武器が壊れて素材集めが途中で終わる",
            "遠出して道に迷う",
            "夜になってゾンビやスケルトンの音にびびる",
            "後ろを振り返ったらクリーパーでずどん",
            "水中に落ちてドラウンドにトライデントされる",
            "遠くからスケルトンに狙い撃ち",
            "エンダーマンと目を合わせて戦闘",
            "ネザー要素は今回はほとんど入れないが、少し出しておいて、そちら側もあるかもと想像させておくこと",
            )


def story_memo(w: World):
    return w.writer_note("物語のメモ",
            "最初は「既にこの世界で生活を始めている」ところから描く",
            "最初の仲間：ゾンビに追いかけられている男子を助ける",
            "最初の女性：夜中にドアが叩かれて、恐怖の中で開けたら女子が立っていた",
            "三人での暮らし：役割分担がうまくできずに口論になる",
            "主人公の特性：主人公だけはクラフト台ではなく、個人の技術を磨いて色々と作っていた",
            "世界説明：クラフト能力だけはゲームに似ているが、それも一部のみで、基本的には現実世界によく似ている",
            "遠出する：生活が安定してきたので果物などの収穫など行動範囲を広げようとする",
            "村発見：小さな規模のものだが村を発見する",
            "交流するのか？：交流賛成派と反対派になって意見がまとまらない",
            "村の使者：村から使者がやってきて、三人は混乱する",
            "村壊滅：一夜にしてすべてがモンスターにやられてしまっていた",
            "人間を滅ぼす存在：村の使者に化けていたのがエンダーワールドの存在。全てを終わらせようとしている。全てがエンダーワールドに飲み込まれてしまうことを願っている。エンダーワールド拡張したい",
            "エンダーの使者を倒すのが一巻の目標",
            "リスポーン作戦は可能か？：ゲームでは何度もリスポーンできるので、武器だけもって特攻を繰り返すことで倒せるが、ここはゲームに似ているが現実世界に思える。死んだらそこで終わりじゃないのか？",
            "一巻ラストはリスポーンが成功したが、そこで衝撃の光景を目撃する、といったところで終わる",
            "生きることは助け合い：一人でも生きていけるというのはただのつよがりでしかなく、誰かを助け、誰かに助けられ、そうやって補い合いながら生きていくしかない。嫌でも",
            )


def chara_memo(w: World):
    return w.writer_note("人物メモ",
            "主人公：一人で黙々とクラフトを楽しむタイプ。元々が人とのかかわりを減らすために始めた",
            "男仲間：みんなでわいわいと楽しみたいが、リアルだと全然駄目。Vチューバーのような仮面をかぶった状態ならはじけられる仮面陽キャ",
            "女仲間：実は建築デザインを勉強していて、そこからクラフトの世界にのめり込んだ。女っぽくないと言われるのが嫌だがゲームの世界なら関係ない",
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            story_memo(w),
            chara_memo(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

