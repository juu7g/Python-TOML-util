# Python-TOML-util

## 概要 Description
TOML設定ファイルユーティリティ  
TOML configuration file utility  

TOML設定ファイルを読んでTkinterのウィジェットで設定画面を作成する。     
Read the TOML configuration file and create a configuration screen with the Tkinter widgets.  

## 特徴 Features

- TOML ファイルを読み書きする  
	Read and write TOML file  
- TOML ファイルに設定値の定義を持たせ画面を作成する  
	仕様についてはプログラムの説明サイトを参照してください  
	Create a screen with the definition of the setting value in the TOML file  
	Please refer to the program description site for specifications  

## TomlFileUtil Class

### 属性 attribute

- `path`：TOML ファイルのパス  
	TOML file path
- `toml_doc`：TOML ファイルを読んで作成した TOML 辞書  
	TOML dictionary created by reading a TOML file
- `_var_dict`：Tkinter variable変数(ウィジェット変数)を値にした辞書  
	create_frame_from_toml_dict() メソッドで返す  
	A dictionary with values as Tkinter variable variables(widget variable)

### メソッド Method

- `dump_toml(self, toml_dict:dict, path:str)`：TOML 辞書を TOMLファイルに出力する  
	Output TOML dictionary to TOML file  
- `save_toml(self, save_path:str="", section:str="", event=None)`：ウィジェット変数の値を section で指定したセクションにコピーして save_path で指定したファイルに保存  
	Copy the value of the widget variable to the section specified by section and save it to the file specified by save_path
- `load_default(self, event=None)`：ウィジェット変数の辞書に TOML 辞書の DEFAULT セクションの値を設定  
Set the value in the DEFAULT section of the TOML dictionary to the dictionary of widget variables  
- `read_toml(self, path:str)`：TOML ファイルを読み込み TOML 辞書を返す  
	Reads a TOML file and returns a TOML dictionary  
- `create_frame_from_toml_dict(self, parent:Any, has_save_button:bool=False, has_default_button:bool=False, is_grid:bool=False)`：TOML 辞書の DEFINITION セクションを読み、画面を作成  
	Read the DEFINITION section of the TOML dictionary and create a screen  
- `set_toml2var_dict(self, section:str)`：TOML 辞書から section で指定したセクションをウィジェット変数の辞書に設定する  
	Set the section specified by section from the TOML dictionary to the dictionary of widget variables  
- `set_var_dict2toml_dict(self, section:str)`：ウィジェット変数の辞書の設定値を TOML 辞書の section で指定したセクションに設定する  
	Set the widget variable dictionary settings to the section specified in section of the TOML dictionary  

### 使い方 Usage

```python
	toml = TomlFileUtil()  
	result = toml.read_toml(file_path)
	create_frame_from_toml_dict(parent)  
```
## 依存関係 Requirement

- Python 3.8.5  
- toml 0.10.2
- tomli 2.0.1
- tomli-w 1.0.0

## インストール方法 Installation

- pip install tomli  
- pip install tomli-w  

## プログラムの説明サイト Program description site

[TOMLで設定ファイルを扱うユーティリティ【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tomlutil)  

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
This software is released under the MIT License, see LICENSE.txt.
