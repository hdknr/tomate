#!/bin/bash

TOMATE_START()
{
    tomato.py  /Users/hide/ve/docs/src/tomate/sample/app start &
}

TOMATE_STOP()
{
    tomato.py  /Users/hide/ve/docs/src/tomate/sample/app stop
}

WEB_START()
{
    python ../manage.py runserver 0.0.0.0:8800
}
