# Python-TOML-util Change Log

## [1.0.2] - 2026-10-19
### Changed

- ログの対応

- TomlFileUtilクラス
	- u_settings属性(USERセクションのデータ)を提供
	- save_toml()メソッドのsectionのデフォルトをUSERにする  
	　　save_pathが未指定の時はself.pathを使用
	- create_frame_from_toml_dict()メソッドの変更
		- 引数 has_v_bar(bool):垂直スクロールバーの有無を追加
		- 引数 align_midashi(bool):見出しの幅を合わせるを追加
		- 引数 bg(str):背景色を追加
		- 戻り値に先頭のエントリーウィジェット(フォーカス設定用)を追加
		- Entryの幅を自動に、位置を左寄せに変更
		- Checkbuttonの幅を自動に、位置を左寄せに変更
	- read_toml()メソッドで例外を通知するよう変更
	- 保存ボタンで保存後メッセージボックスを表示するよう変更

### Added
- SettingDialogクラスを提供

## [1.0.1] - 2025-09-11
### Changed
- Python 3.12.8, tomli-w 1.2.0対応  
	tomliに代わり、tomllibを使用するように変更  

