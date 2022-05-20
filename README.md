# Python-TOML-util

## �T�v Description
TOML�ݒ�t�@�C�����[�e�B���e�B  
TOML configuration file utility  

TOML�ݒ�t�@�C����ǂ��Tkinter�̃E�B�W�F�b�g�Őݒ��ʂ��쐬����B     
Read the TOML configuration file and create a configuration screen with the Tkinter widgets.  

## ���� Features

- TOML �t�@�C����ǂݏ�������  
	Read and write TOML file  
- TOML �t�@�C���ɐݒ�l�̒�`����������ʂ��쐬����  
	�d�l�ɂ��Ă̓v���O�����̐����T�C�g���Q�Ƃ��Ă�������  
	Create a screen with the definition of the setting value in the TOML file  
	Please refer to the program description site for specifications  

## TomlFileUtil Class

### ���� attribute

- `path`�FTOML �t�@�C���̃p�X  
	TOML file path
- `toml_doc`�FTOML �t�@�C����ǂ�ō쐬���� TOML ����  
	TOML dictionary created by reading a TOML file
- `_var_dict`�FTkinter variable�ϐ�(�E�B�W�F�b�g�ϐ�)��l�ɂ�������  
	create_frame_from_toml_dict() ���\�b�h�ŕԂ�  
	A dictionary with values as Tkinter variable variables(widget variable)

### ���\�b�h Method

- `dump_toml(self, toml_dict:dict, path:str)`�FTOML ������ TOML�t�@�C���ɏo�͂���  
	Output TOML dictionary to TOML file  
- `save_toml(self, save_path:str="", section:str="", event=None)`�F�E�B�W�F�b�g�ϐ��̒l�� section �Ŏw�肵���Z�N�V�����ɃR�s�[���� save_path �Ŏw�肵���t�@�C���ɕۑ�  
	Copy the value of the widget variable to the section specified by section and save it to the file specified by save_path
- `load_default(self, event=None)`�F�E�B�W�F�b�g�ϐ��̎����� TOML ������ DEFAULT �Z�N�V�����̒l��ݒ�  
Set the value in the DEFAULT section of the TOML dictionary to the dictionary of widget variables  
- `read_toml(self, path:str)`�FTOML �t�@�C����ǂݍ��� TOML ������Ԃ�  
	Reads a TOML file and returns a TOML dictionary  
- `create_frame_from_toml_dict(self, parent:Any, has_save_button:bool=False, has_default_button:bool=False, is_grid:bool=False)`�FTOML ������ DEFINITION �Z�N�V������ǂ݁A��ʂ��쐬  
	Read the DEFINITION section of the TOML dictionary and create a screen  
- `set_toml2var_dict(self, section:str)`�FTOML �������� section �Ŏw�肵���Z�N�V�������E�B�W�F�b�g�ϐ��̎����ɐݒ肷��  
	Set the section specified by section from the TOML dictionary to the dictionary of widget variables  
- `set_var_dict2toml_dict(self, section:str)`�F�E�B�W�F�b�g�ϐ��̎����̐ݒ�l�� TOML ������ section �Ŏw�肵���Z�N�V�����ɐݒ肷��  
	Set the widget variable dictionary settings to the section specified in section of the TOML dictionary  

### �g���� Usage

```python
	toml = TomlFileUtil()  
	result = toml.read_toml(file_path)
	create_frame_from_toml_dict(parent)  
```
## �ˑ��֌W Requirement

- Python 3.8.5  
- toml 0.10.2
- tomli 2.0.1
- tomli-w 1.0.0

## �C���X�g�[�����@ Installation

- pip install tomli  
- pip install tomli-w  

## �v���O�����̐����T�C�g Program description site

[TOML�Őݒ�t�@�C�����������[�e�B���e�B�yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/tomlutil)  

## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
This software is released under the MIT License, see LICENSE.txt.
