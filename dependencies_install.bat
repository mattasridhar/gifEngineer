@ECHO off
setLocal
rem dependencies_install.bat - One stop installer for the required libraries for this application.
SET header=------------------------------------------------
SET tagger=*****

:INIT
rem Checking if python is properly installled and its path is appropriately set.
ECHO %tagger% CHECKING PYTHON AVAILABIITY! %tagger%
ECHO %header%
ECHO.
python.exe --version >NUL 2>&1
IF ERRORLEVEL 1 GOTO MISSINGPYTHON
ECHO %tagger% Detected Python Version: %tagger%
FOR /F "tokens=*" %%a IN ('python --version') DO SET pyVersion=%%a
GOTO UPDATEPIP
GOTO EXITBATCH

:UPDATEPIP
rem Update PIP if needed
ECHO.
ECHO %tagger% UPDATING PIP! %tagger%
ECHO %header%
python -m pip install --upgrade pip
IF ERRORLEVEL 1 GOTO UPDATEFAILED
GOTO INSTALLLIBRARIES

:INSTALLLIBRARIES
rem Installing the dependent libraries
ECHO.
ECHO %tagger% INSTALLING PYINSTALLER! %tagger%
ECHO %header%
pip install -U pyinstaller
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% PYINSTALLER library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING PY2APP! %tagger%
ECHO %header%
pip install -U py2app
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% PY2APP library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING MOVIEPY! %tagger%
ECHO %header%
pip install MoviePy
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% MOVIEPY library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING TKINTER! %tagger%
ECHO %header%
pip install tkinter
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% TKINTER library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING OPEN-CV! %tagger%
ECHO %header%
pip install opencv-python
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% OPEN-CV library %tagger%
	GOTO INSTALLATIONERROR
)

GOTO EXITBATCH

:MISSINGPYTHON
rem Python is not found. Showing message and exiting the batch execution.
ECHO.
ECHO %tagger% MISSING PYTHON! %tagger%
ECHO %header%
ECHO Python.exe either not installed or PATH is not set.
ECHO Manually install python and execute this batch file again.
ECHO %header%
GOTO EXITBATCH

:UPDATEFAILED
rem update of PIP failed.
ECHO.
ECHO %tagger% PIP UPDATE FAILED! %tagger%
ECHO %header%
ECHO 'pip' update failed. Do you want to continue with Installing the libraries?
SET /P option=Press 'Y' for YES and 'N' for NO:
IF %input% EQU Y (
	ECHO %tagger% Initiating the installation of dependent libraries. %tagger%
	GOTO INSTALLLIBRARIES
) ELSE IF %input% EQU N (
	ECHO %tagger% Terminating the installation of dependent libraries. %tagger%
	GOTO EXITBATCH
) ELSE (
	ECHO %tagger% Incorrect Option. Please select proper option[Y or N].
	GOTO UPDATEFAILED
)
GOTO EXITBATCH

:INSTALLATIONERROR
rem Installation of libraries failed. Showing message and reqesting for retry.
ECHO.
ECHO If the installation is not successful, check if version is greater than 3.0 or not.
ECHO or simply install python and try again.
ECHO.
GOTO RETRY

:RETRY
rem Requesting User for attempting again with the installation of the libraries. Show apt messages. Also accept input from user.
ECHO %header%
ECHO ERROR occured while installing dependent libraries.
ECHO Would you prefer re-attempting on the dependency installation?
SET /P input=Press 'Y' for YES and 'N' for NO:
IF %input% EQU Y (
	ECHO %tagger% Re-initiating the installation of dependent libraries. %tagger%
	GOTO INSTALLLIBRARIES
) ELSE IF %input% EQU N (
	ECHO %tagger% Terminating the installation of dependent libraries. %tagger%
	GOTO EXITBATCH
) ELSE (
	ECHO %tagger% Incorrect Option. Please select proper option[Y or N].
	GOTO RETRY
)
GOTO EXITBATCH


:EXITBATCH
ECHO %tagger% Exiting batch execution %tagger%
pause
endlocal
