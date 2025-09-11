"""
TOML設定ファイル作成
"""
import sys
sys.path.append("..")
from toml_libs_juu7g import toml_file_util

class TomlFileCreate:
    """
    tomlファイル作成用クラス
    """
    def __init__(self) -> None:
        self.tomlu = toml_file_util.TomlFileUtil()

    def add_new_item(self, settings:dict, new_item:tuple):
        """
        新しい項目がないなら追加する

        Args:
            settings(dict):     設定用辞書
            new_item(tuple):    (キー名1, キー名2, 説明, 型, デフォルト値)
        Returs:
            dict:   追加後の辞書
            bool:   既存だったかの結果
        """
        key1, key2, exp, type, init_v = new_item
        has_key = key2 in settings['DEFINITION'][key1]
        settings['DEFINITION'][key1].setdefault(key2, (exp, type))
        settings['DEFAULT'][key1].setdefault(key2, init_v)
        settings['USER'][key1].setdefault(key2, init_v)
        return settings, has_key

    def create_toml(self, path:str):
        """
        tomlファイルを作成する
        出力内容を辞書でロジックに定義
        tomlファイルを手作業で作ってうまく読めないと悩むより辞書から作った方が間違いないから
        tomlをjsonにすれば転用できるかも
        """
        toml_data = {}
        toml_data['DEFINITION'] = {
            "画像変換":{        "do_resize":["サイズ変更する", "bool"]
                            , "dest_path":["保存先フォルダ", "str"]
                            , "width":["幅", "int"]
                            , "height":["高さ", "int"]
                            , "overwrite":["新しいファイルをいくつも作らない", "bool"]
                            , "exif":["Exif情報出力", "bool"]
                            , "mirror":["ミラー反転", "bool"]
                            , "rotate270":["右回転", "bool"]
                            , "rotate90":["左回転", "bool"]
                            # , "to_webp":["WebPに変換", "bool"]
                    }, 
            "透かし":{     "is_water_mark":["透かし文字付加", "bool"]
                            , "water_mark":["透かし文字", "str"]	
                            , "wm_font_name":["フォントファイル名", "str"]
                            , "wm_size":["フォントサイズ", "int"]
                            , "wm_f_color":["文字色", "str"]
                            , "wm_b_color":["縁取りの色", "str"]
                            , "wm_stroke":["縁取りの幅(px)", "int"]
                            , "wm_padx":["右下からの隙間(横)", "int"]
                            , "wm_pady":["右下からの隙間(縦)", "int"]
                        }, 
            "アップロード":{        "use_hatena_folder":["デフォルトフォルダを使用", "bool"]
                            , "folder":["フォトライフのフォルダ", "str"]
                            },
            "画像URLのコピー":{           "foto":["fotolife記法で出力", "bool"]
                            , "only_url":["画像番号またはURLだけを出力", "bool"]
                            , "add_title":["ファイル名をタイトルとして付加", "bool"]
                            , "add_options":["オプション", "str"]
                    },
            "表示設定":{       "width4thumbnail":["サムネイル画像の幅", "int"]
                            , "geometry":["アプリのサイズと位置", "str"]
                    }
            }
        toml_data['DEFAULT'] = {
            "画像変換":{        "do_resize":True
                            , "dest_path":"."
                            , "width":800
                            , "height":0
                            , "overwrite":True
                            , "exif":False
                            , "mirror":False
                            , "rotate270":False
                            , "rotate90":False
                    }, 
            "透かし":{     "is_water_mark":False
                            , "water_mark":""				# 透かしの指定(""なら入れない)
                            , "wm_font_name":"msgothic.ttc"	# フォントファイル名
                            , "wm_size":12				    # フォントサイズ
                            , "wm_f_color":"gold"			# 文字色
                            , "wm_b_color":"black"			# 縁取りの色
                            , "wm_stroke":0					# 縁取りの幅(px)
                            , "wm_padx":5					# 右下からの隙間
                            , "wm_pady":5					# 右下からの隙間
                        }, 
            "アップロード":{        "use_hatena_folder":True
                            , "folder":""
                            },
            "画像URLのコピー":{           "foto":False      # fotolife記法で出力
                            , "only_url":False  # 画像番号またはURLだけを出力
                            , "add_title":True  # ファイル名をタイトルとして付加
                            , "add_options":""  # オプション
                    },
            "表示設定":{       "width4thumbnail":250
                            , "geometry":"1000x702+0+0"
                    }
            }
        toml_data['USER'] = {
            "画像変換":{        "do_resize":True
                            , "dest_path":"."
                            , "width":800
                            , "height":0
                            , "overwrite":True
                            , "exif":False
                            , "mirror":False
                            , "rotate270":False
                            , "rotate90":False
                    }, 
            "透かし":{     "is_water_mark":False
                            , "water_mark":""				# 透かしの指定(""なら入れない)
                            , "wm_font_name":"msgothic.ttc"	# フォントファイル名
                            , "wm_size":12				    # フォントサイズ
                            , "wm_f_color":"gold"			# 文字色
                            , "wm_b_color":"black"			# 縁取りの色
                            , "wm_stroke":0					# 縁取りの幅(px)
                            , "wm_padx":5					# 右下からの隙間
                            , "wm_pady":5					# 右下からの隙間
                        }, 
            "アップロード":{        "use_hatena_folder":True
                            , "folder":""
                            },
            "画像URLのコピー":{           "foto":False      # fotolife記法で出力
                            , "only_url":False  # 画像番号またはURLだけを出力
                            , "add_title":True  # ファイル名をタイトルとして付加
                            , "add_options":""  # オプション
                    },
            "表示設定":{       "width4thumbnail":250
                            , "geometry":"1000x702+0+0"
                    }
            }

        self.tomlu.dump_toml(toml_data, path)

    def create_toml_sample(self, path:str):
        """
        tomlファイルを作成する
        出力内容を辞書でロジックに定義
        tomlファイルを手作業で作ってうまく読めないと悩むより辞書から作った方が間違いないから
        tomlをjsonにすれば転用できるかも
        """
        toml_data = {}
        toml_data['DEFINITION'] = {
            "セクション1":{    "key1":["key1の説明", "bool"]
                            , "key2":["key2の説明", "str"]
                            , "key3":["key3の説明", "int"]
                    }, 
            "セクション2":{    "key4":["key4の説明", "bool"]
                            , "key5":["key5の説明", "str"]	
                            , "key6":["key6の説明", "str"]
                        }, 
            "セクション3":{    "key7":["key7の説明", "bool"]
                            , "key8":["key8の説明", "str"]
                            }
            }
        toml_data['DEFAULT'] = {
            "セクション1":{    "key1":True
                            , "key2":"文字列2"
                            , "key3":800
                    }, 
            "セクション2":{    "key4":False
                            , "key5":"文字列5"	
                            , "key6":"文字列6"
                        }, 
            "セクション3":{    "key7":True
                            , "key8":"文字列8"
                            }
            }
        toml_data['USER'] = {
            "セクション1":{    "key1":True
                            , "key2":"文字列2"
                            , "key3":800
                    }, 
            "セクション2":{    "key4":False
                            , "key5":"文字列5"	
                            , "key6":"文字列6"	
                        }, 
            "セクション3":{    "key7":True
                            , "key8":"文字列8"
                            }
            }

        self.tomlu.dump_toml(toml_data, path)

if __name__ == '__main__':
    toml = TomlFileCreate()
    is_add = False
    if is_add:
        path = "blog_image_tool_base.toml"
        settings = toml.tomlu.read_toml(path)
        new_item = ("画像変換", "to_webp", "WebPに変換", "bool", False)
        settings, has_key = toml.add_new_item(settings, new_item)
        if not has_key:
            toml.tomlu.dump_toml(settings, path)
    else:
        toml.create_toml('blog_image_tool_base.toml')
        toml.create_toml_sample('example.toml')