"""
TOML設定ファイル作成
"""

import toml_file_util

class TomlFileCreate:
    """
    tomlファイル作成用クラス
    """
    def __init__(self) -> None:
        self.tomlu = toml_file_util.TomlFileUtil()
        
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
    toml.create_toml_sample('example.toml')