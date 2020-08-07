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
MAJOR, MINOR, MICRO = 0, 1, 0
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
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            )


# Notes
def writer_note(w: World):
    return w.writer_note("作者の覚書",
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

