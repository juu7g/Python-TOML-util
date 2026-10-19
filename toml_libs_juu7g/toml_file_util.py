"""
TOML設定ファイルユーティリティ
"""
from logging import getLogger, StreamHandler, Formatter, DEBUG
logger = getLogger(__name__)

from logging import exception
from typing import Any, Tuple
import tomllib, tomli_w
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font as tkFont
from tkinter import simpledialog, messagebox
from tkinter_libs_juu7g.tkinter_libs import ScrolledFrame
import sys

class TomlFileUtil:
    """
    tomlファイル操作、設定画面サポートユーティリティ

    Attributes:
        path(str):          tomlファイルのパス
        toml_doc(dict):     tomlファイルを読んで作成した辞書
        u_settings(dict):   USERセクションを平坦化した設定用辞書
        _var_dict(dict):    Tkinter variable変数(ウィジェット変数)を値にした辞書
    """
    def __init__(self) -> None:
        self.path = ""          # tomlファイルのパス
        self.toml_doc = {}      # tomlファイルを読んで作成した辞書
        self.u_settings = {}    # USERセクションを平坦化した設定用辞書
        self._var_dict = {}     # Tkinter variable変数(ウィジェット変数)を値にした辞書

    def dump_toml(self, toml_dict:dict, path:str):
        """
        tomlで読み込んだ辞書をtomlファイルに出力する

		Args:
            toml_dict(dict):tomlで読み込んだ辞書
            path(str):      保存先ファイル名
        """
        try:
            with open(path, 'wb') as configfile:
                tomli_w.dump(toml_dict, configfile)
        except exception as e:
            print(e)

    def save_toml(self, save_path:str="", section:str="USER", event=None):
        """
        ウィジェット変数の値をsectionで指定したセクションに移してsave_pathで指定したファイルに保存
            引数なしは読んだ時のパスにUSERセクションを保存

		Args:
            save_path(str): 保存先ファイル名(空の場合self.pathを使用(読んだ時のパス))
            section(str):   保存先セクション
        """
        if not save_path:
            save_path = self.path
        self.set_var_dict2toml_dict(section)
        self.dump_toml(self.toml_doc, save_path)
        messagebox.showinfo("保存", f"設定を{save_path}に保存しました。", parent=self.parent)

    def load_default(self, event=None):
        """
        ウィジェット変数の辞書にTOMLのDEFAULTセクションの値を設定
        """
        self.set_toml2var_dict("DEFAULT")

    def read_toml(self, path:str) -> dict:
        """
        tomlファイルを読み込み辞書を返し、toml_doc属性に保持
        平坦化した設定用辞書をu_settings属性に保持
        引数pathをpath属性に保持

		Args:
            path(str):    読み込むファイル名
		Returns:
			dict:   tomlファイルの辞書。
        """
        self.path = path
        # try:
        with open(path, "rb") as f:
            toml_dict = tomllib.load(f) # 例外あり

        self.toml_doc = toml_dict
        new_d = {}

        # グループ化されているTOMLデータ辞書を平坦化
        for d in self.toml_doc.get('USER').values():
            new_d |= d
        self.u_settings = new_d     # 平坦化した設定用辞書

        return toml_dict

    def entry_validate(self, action:str, modify_str:str) -> bool:
        """
        エントリーの入力検証

        Args:
            action(str):    アクション(削除：0、挿入：1、その他：-1)
            modify_str(str):挿入、削除されるテキスト
        """
        if action != "1": return True   # 挿入の時だけ検証
        return modify_str.isdigit()     # 数字かどうか

    def create_frame_from_toml_dict(self, parent:Any
        , has_v_bar:bool
        , has_save_button:bool=False, has_default_button:bool=False, is_grid:bool=False, align_midashi:bool=True, bg:str="lightblue") -> Tuple[dict, any]:
        """
        tomlデータ(toml_cod属性)からDEFINITIONセクション(キー:[説明, 型]の辞書)を抜き出し、フレームを作成
        tomlデータは事前に読んでおく
        ※保存ボタンを表示する場合、ボタンに割り付けるメソッドを後から指定する
            例 obj.btn_save.config(command=lambda path=my_path: toml.save_toml(path, "USER"))

		Args:
            parent(Any):                主にFrame 親コンテナ
            has_v_bar(bool):            垂直スクロールバーの有無
            has_save_button(bool):      保存用ボタンの有無
            has_default_button(bool):   デフォルトに戻すボタンの有無
            is_grid(bool):              labelとentryを横並びにするかどうか
            align_midashi(bool):        見出しの幅を合わせる
            bg(str):                    背景色
		Returns:
			dict:   ウィジェット変数の辞書
            widget: フォーカスさせるウィジェット
        """
        self.parent = parent
        if has_v_bar:   # 垂直スクロールバーの有無
            # ScrolledFrameでラップする
            sf = ScrolledFrame(parent, has_h_bar=True, bg=bg)
            sf.parent_frame.pack(fill=tk.BOTH, expand=True)
            hosei = 16 + 5 # スクロールバーの分短いようなので補正
        else:
            sf = tk.Frame(parent, bg=bg)
            sf.pack(fill=tk.BOTH, expand=True)
            hosei = 0

        toml_dict = self.toml_doc["DEFINITION"]
        # self._var_dict = {}
        # 説明の最大文字数を求める
        max_length = max([len(v2[0]) for v1 in toml_dict.values() for v2 in v1.values()])
        focus_w = None
        for group_key, group_item in toml_dict.items():
            label_frame = tk.LabelFrame(sf, text=group_key, padx=5, pady=5)
            for i, (k, item) in enumerate(group_item.items()):
                if item[1] == "str":
                    self._var_dict[k] = tk.StringVar()
                    entry_ = tk.Entry(label_frame, textvariable=self._var_dict[k], width=-1)
                elif item[1] == "int":
                    self._var_dict[k] = tk.IntVar()
                    entry_ = tk.Entry(label_frame, textvariable=self._var_dict[k]
                            , validate="key", vcmd=(sf.register(self.entry_validate), "%d", "%S"), width=-1)
                elif item[1] == "bool":
                    self._var_dict[k] = tk.BooleanVar()
                    checkbutton_ = tk.Checkbutton(label_frame, variable=self._var_dict[k]
                        , text=item[0], anchor="w")
                    if is_grid:
                        checkbutton_.grid(row=i, column=0, columnspan=2 , sticky="w")
                    else:
                        checkbutton_.pack(anchor="w")
                    continue    # ラベルは作らない
                label_ = tk.Label(label_frame, text=item[0])
                # pack,grid
                if is_grid:
                    label_.grid(row=i, column=0, sticky="e")
                    entry_.grid(row=i, column=1, sticky="w")
                else:
                    label_.pack(anchor="w")
                    entry_.pack(anchor="w", padx=(40, 0), fill="x")
                if focus_w is None:
                    focus_w = entry_
            if is_grid and align_midashi:     # 見出しの幅を合わせる
                label_frame.columnconfigure(0, weight=1)    # grid column 0 の余白を引き延ばす
            label_frame.pack(fill="x", padx=5,pady=5, expand=True)
            label_frame.update_idletasks()

        # 保存ボタンの作成
        if has_save_button:
            self.btn_save = tk.Button(sf, text="設定保存", 
                command=self.save_toml)
            self.btn_save.pack(side="bottom")

        # デフォルトロードボタンの作成
        if has_default_button:
            self.btn_default = tk.Button(sf, text="デフォルトに戻す"
                , command=self.load_default)
            self.btn_default.pack(side="bottom")

        # sf.update_idletasks()
        return self._var_dict, focus_w

    def set_toml2var_dict(self, section:str):
        """
        tomlの辞書からsectionで指定したセクションをウィジェット変数の辞書に設定する

		Args:
            section(str):    セクション
        """
        for group_item in self.toml_doc[section].values():
            for k, item in group_item.items():
                self._var_dict[k].set(item)

    def set_var_dict2toml_dict(self, section:str):
        """
        ウィジェット変数の辞書(self._var_dict)の設定値を
        tomlの辞書(self.toml_doc)のsectionで指定したセクションに設定する
        同時に平坦化した設定用辞書(self.settings)にも設定

		Args:
            section(str):    セクション
        """
        for group_item in self.toml_doc[section].values():
            for k in group_item:
                v = self._var_dict.get(k).get()
                group_item[k] = v
                if section == "USER":
                    self.u_settings[k] = v

class SettingDialog(simpledialog.Dialog):
    """
    設定ダイアログ

    属性:
        toml(TomlfileUtil): TomlfileUtilクラスインスタンス
        height(int): ダイアログの高さ
        has_v_bar(bool): 垂直スクロールバーの有無
        has_save_button(bool): 保存ボタンの有無
        has_default_button(bool): デフォルトボタンの有無
        result: 結果(OKが押されたかどうか)
        
    """
    def __init__(self, parent, toml:TomlFileUtil, title = None, height=None, has_v_bar:bool=False, has_save_button:bool=False, has_default_button:bool=False,):
        """
        設定ダイアログ

        Args:
            parent: 親ウィジェット
            toml(TomlfileUtil): TomlfileUtilクラスインスタンス
            title(str): タイトル
            height(int): ダイアログの高さ
            has_v_bar(bool): 垂直スクロールバーの有無
            has_save_button(bool):保存ボタンの有無
            has_default_button(bool):デフォルトボタンの有無
        """
        self.toml = toml
        self.height = height
        self.has_v_bar = has_v_bar
        self.has_save_button = has_save_button
        self.has_default_button = has_default_button
        super().__init__(parent, title)
    
    def body(self, master):
        """
        ファイルを読んで設定を画面表示
        設定項目の辞書を返す

        Args:
            master(widget):  親ウィジェット
        """
        # 設定画面フレームを作成。戻り値は変数の辞書        
        _, w = self.toml.create_frame_from_toml_dict(self, self.has_v_bar, self.has_save_button, self.has_default_button, True, False)

        self.toml.set_toml2var_dict("USER")
        self.update_idletasks()

        return w

    def grab_set(self):
        """
        ダイアログの表示位置を設定(bodyでは機能しないため)
        """
        # フォーカス先のエントリーの親から幅を取得、スクロールバーの幅と余白を加算
        if isinstance(self.initial_focus.master.master, ScrolledFrame):
            w = self.initial_focus.master.winfo_width() + 16 + 15
        else:
            w = self.winfo_width()
        h = self.height if self.height is not None else self.winfo_height()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw // 2) - (w // 2)
        y = (sh // 2) - (h // 2)
        logger.debug(f"set geometry:{self.geometry()} to {w}x{h}+{x}+{y}")
        self.geometry(f'{w}x{h}+{x}+{y}')

        return super().grab_set()

    def apply(self):
        """
        OKボタンが押された時の処理
        """
        # 画面の入力内容を反映
        self.toml.set_var_dict2toml_dict("USER")
        self.result = True

if __name__ == '__main__':
    # logger setting
    LOGLEVEL = "DEBUG"   # ログレベル('CRITICAL','FATAL','ERROR','WARN','WARNING','INFO','DEBUG','NOTSET')
    logger = getLogger()
    handler = StreamHandler()	# このハンドラーを使うとsys.stderrにログ出力
    handler.setLevel(LOGLEVEL)
    # ログ出形式を定義 時:分:秒.ミリ秒 L:行 M:メソッド名 T:スレッド名 コメント
    fmt = Formatter("{asctime}.{msecs:.0f} : {message}", "%H:%M:%S", "{")
    if logger.isEnabledFor(DEBUG):
        fmt = Formatter("{asctime}.{msecs:.0f} {name} L:{lineno:0=3} T:{threadName} M:{funcName} : {message}", "%H:%M:%S", "{")
    handler.setFormatter(fmt)
    logger.setLevel(LOGLEVEL)
    logger.addHandler(handler)
    # logger.propagate = False
    logger.debug("start log")

    def show(parent, toml):
        sd = SettingDialog(parent, toml, "設定", has_v_bar=True, has_save_button=True)
        if sd.result:
            print(f"{toml.u_settings=}")   # 設定画面の変更を表示

    toml = TomlFileUtil()

    # ファイルから編集画面を作成し起動
    if len(sys.argv) < 2:  
        print("引数にファイルを指定してください。")
        sys.exit()
    my_path = sys.argv[1]
    toml_doc = toml.read_toml(my_path)  # 例外あり

    root = tk.Tk()
    box = tk.Frame(root)
    box.pack()
    btn = tk.Button(root, text="ダイアログ表示")
    btn.config(command=lambda p=box, t=toml: show(p, t))
    btn.pack()
    var_dict, _ = toml.create_frame_from_toml_dict(box, True, True, True)
    box.update_idletasks()

    logger.debug(f"1:{root.geometry()}")
    g = root.geometry()
    root.geometry(g)
    logger.debug(f"2:{root.geometry()}")
    toml.set_toml2var_dict("USER")
    toml.btn_save.config(command=lambda path=my_path: toml.save_toml(path, "USER"))
    root.mainloop()