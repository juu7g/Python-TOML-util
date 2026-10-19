# Python-TOML-util

## 概要
TOML設定ファイルユーティリティ  

TOML設定ファイルを読んでTkinterのウィジェットで設定画面を作成する。     

## 特徴

- TOML ファイルを読み書きする  
- TOML ファイルに設定値の定義を持たせ画面を作成する  
	仕様についてはプログラムの説明サイトを参照してください  

## TomlFileUtil Class
tomlファイル操作、設定画面を作成するクラス

### 属性

- `path`：TOML ファイルのパス  
- `toml_doc`：TOML ファイルを読んで作成した TOML 辞書  
- `_var_dict`：Tkinter variable変数(ウィジェット変数)を値にした辞書  
	create_frame_from_toml_dict() メソッドで返す  

### メソッド

- `dump_toml(self, toml_dict:dict, path:str)`：TOML 辞書を TOMLファイルに出力する  
- `save_toml(self, save_path:str="", section:str="", event=None)`：ウィジェット変数の値を section で指定したセクションにコピーして save_path で指定したファイルに保存  
- `load_default(self, event=None)`：ウィジェット変数の辞書に TOML 辞書の DEFAULT セクションの値を設定  
- `read_toml(self, path:str)`：TOML ファイルを読み込み TOML 辞書を返す  
- `create_frame_from_toml_dict(self, parent:Any, has_v_bar:bool, has_save_button:bool=False, has_default_button:bool=False, is_grid:bool=False, align_midashi:bool=True, bg:str="lightblue")`：TOML 辞書の DEFINITION セクションを読み、画面を作成  
- `set_toml2var_dict(self, section:str)`：TOML 辞書から section で指定したセクションをウィジェット変数の辞書に設定する  
- `set_var_dict2toml_dict(self, section:str)`：ウィジェット変数の辞書の設定値を TOML 辞書の section で指定したセクションに設定する  

### 使い方

```python
	toml = TomlFileUtil()  
	result = toml.read_toml(file_path)
	root = tk.Tk()
	vars = toml.create_frame_from_toml_dict(root)  
```
## SettingDialog Class
TomlFileUtilクラスのcreate_frame_from_toml_dict()メソッドで作成した画面をダイアログとして提供するクラス  
tomlファイルを読んでコンストラクタを呼ぶことで設定内容を修正可能なダイアログとして表示します。

### 継承
- `simpledialog.Dialog`

### 属性

- `toml(TomlfileUtil)`: TomlfileUtilオブジェクト
- `height(int)`: ダイアログの高さ
- `has_v_bar(bool)`: 垂直スクロールバーの有無
- `has_save_button(bool)`: 保存ボタンの有無
- `has_default_button(bool)`: デフォルトボタンの有無
- `result`: 結果(OKが押されたかどうか)  

### コンストラクタ
`SettingDialog(parent, toml:TomlFileUtil, title = None, height=None, has_v_bar:bool=False, has_save_button:bool=False, has_default_button:bool=False)`

#### 引数
- parent: 親ウィジェット
- toml(TomlfileUtil): TomlfileUtilクラスインスタンス
- title(str): タイトル
- height(int): ダイアログの高さ
- has_v_bar(bool): 垂直スクロールバーの有無
- has_save_button(bool):保存ボタンの有無
- has_default_button(bool):デフォルトボタンの有無

### オーバーロードしているメソッド

- `body(self, master)`：画面作成  
	TomlfileUtilクラスの`create_frame_from_toml_dict()`メソッドで作成。  
	作成後、toml属性のUSERセクションの値を設定  
	最初のEntryウィジェットをフォーカス位置として返す
- `grab_set(self)`：ダイアログの表示位置を設定  
- `apply(self)`：OKボタンが押された時の処理  
	画面で設定された値をtoml属性に反映  
	result属性をTrueに設定

### 使い方

```python
    sd = SettingDialog(self.view, self.view.toml, "設定", height=800, has_v_bar=True, has_save_button=True)
    if sd.result:
        self.on_toml_change()	# 設定画面の変更を反映
```
## 依存関係

- Python 3.12.8  
- tomli-w 1.2.0

## インストール方法

- Install: pip install git+https://github.com/juu7g/Python-TOML-util.git  
- Import : from toml_libs_juu7g.toml_file_util import TomlFileUtil

## プログラムの説明サイト

[TOMLで設定ファイルを扱うユーティリティ【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tomlutil)  

## 作者
juu7g

## ライセンス
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
