# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:58:58 2022

@author: cihan
"""

import spacy
import spacy_streamlit


def app():
        
    try:
        models = ["en_core_web_md"]
    except: # If not present, we download
        spacy.cli.download("en_core_web_md")
        models = ["en_core_web_md"]    
        
    
    default_text = ""
        
    spacy_streamlit.visualize(models, default_text, visualizers=["ner"],
                              show_pipeline_info=False, show_config=False,
                              show_json_doc=False, show_meta=False,
                              ner_attrs = ["text", "label_"])


if __name__ == '__main__':
    app()