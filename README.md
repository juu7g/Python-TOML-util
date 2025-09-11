# Python-TOML-util

## 概要
TOML設定ファイルユーティリティ  

TOML設定ファイルを読んでTkinterのウィジェットで設定画面を作成する。     

## 特徴

- TOML ファイルを読み書きする  
- TOML ファイルに設定値の定義を持たせ画面を作成する  
	仕様についてはプログラムの説明サイトを参照してください  

## TomlFileUtil Class

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
- `create_frame_from_toml_dict(self, parent:Any, has_save_button:bool=False, has_default_button:bool=False, is_grid:bool=False)`：TOML 辞書の DEFINITION セクションを読み、画面を作成  
- `set_toml2var_dict(self, section:str)`：TOML 辞書から section で指定したセクションをウィジェット変数の辞書に設定する  
- `set_var_dict2toml_dict(self, section:str)`：ウィジェット変数の辞書の設定値を TOML 辞書の section で指定したセクションに設定する  

### 使い方

```python
	toml = TomlFileUtil()  
	result = toml.read_toml(file_path)
	root = tk.Tk()
	vars = toml.create_frame_from_toml_dict(root)  
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
