Stock Screener Model
========================

This is a simple model built using `FastAPI <https://fastapi.tiangolo.com/>`_ to demonstrate the effectiveness of the library.

`Learn more <https://github.com/amruthvvkp/stock_screener_fastapi>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/amruthvvkp/stock_screener_fastapi/blob/master/setup.py>`_.

Usage Instructions
=======================
1. Install Python 3.7 or above.
2. For required dependencies refer ``requirements.txt`` `click here <https://github.com/amruthvvkp/stock_screener_fastapi/blob/feature/master/requirements.txt>`_.
3. From terminal run -
    * Navigate to the path - cd ../stock_screener_fastapi/model
    * Run `Uvicorn <https://www.uvicorn.org/>`_ server - uvicorn main:app --reload
4. Open the following -
    * Web App - http://127.0.0.1:8000
    * Interactive API Docs (`Swagger <https://github.com/swagger-api/swagger-ui>`_) - http://127.0.0.1:8000/docs
    * Alternative API Docs (`ReDoc <https://github.com/Redocly/redoc>`_) - http://127.0.0.1:8000/redoc

Notes
======
* Values are stored in a Sqlite3 database locally.

