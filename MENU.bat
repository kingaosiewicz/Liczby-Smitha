@echo off
:menu
cls
echo ======MENU======
echo 1. START
echo 2. INFORMACJE
echo 3. BACKUP
echo 4. ZAKONCZ
echo ================
set /p select="Wybierz 1,2,3,4: "

if "%select%"=="" goto invalid
if "%select%"=="1" goto start
if "%select%"=="2" goto informacje
if "%select%"=="3" goto backup
if "%select%"=="4" goto exit

:invalid
echo Wybierz opcje (1-4)
pause
goto menu

:start
echo Wybrales opcje START

REM Przetwarzanie plików z katalogu Input
for /f "delims=" %%a in ('dir /b Input') do (
    echo Otwieram plik %%a
    call C:\Users\conta\AppData\Local\Programs\Python\Python313\python.exe main.py %%a
)

REM Generowanie raportu
call C:\Users\conta\AppData\Local\Programs\Python\Python313\python.exe raport.py

pause
goto menu

:informacje
echo Wybrales opcje INFORMACJE
echo.
echo Liczba Smitha to liczba naturalna zlozona, ktorej suma cyfr jest rowna sumie cyfr wszystkich liczb wystepujacych w jej  rozkladzie na czynniki pierwsze. Na przyklad 202 jest liczba Smitha, poniewaz 2 + 0 + 2 = 4, a po jej rozkladzie na    
echo czynniki pierwsze 202 = 2 * 101 suma cyfr obu czynnikow wynosi 2 + 1 + 0 + 1 = 4. Program weryfikuje, czy podana liczba naturalna jest liczba Smitha. W tym celu wykonywane sa funkcje obliczajace sume cyfr liczby, sprawdzajace, czy liczba
echo jest pierwsza, oraz wyznaczajace wszystkie dzielniki pierwsze. Korzystajac z wynikow poprzednich funkcji, glowna funkcjaprogramu weryfikuje, czy liczba spelnia warunki definicji liczby Smitha: musi byc zlozona, a suma cyfr liczby musi
echo rownac sie sumie cyfr jej dzielnikow pierwszych. Program przetwarza pliki wejsciowe z katalogu "Input", gdzie kazda 
echo linia zawiera liczbe do sprawdzenia, i zapisuje wyniki w odpowiednich plikach wyjsciowych w katalogu "Output",
echo informujac, czy liczba jest liczba Smitha.
echo.
pause
goto menu

:backup
echo Wybrales opcje BACKUP
IF NOT EXIST backups mkdir backups
set name=%date%--%TIME:~0,2%-%TIME:~3,2%-%TIME:~6,2%
set name=%name::=-%
IF EXIST Raport_Smith.html mkdir backups\%name%
robocopy Input backups\%name%\Input /NFL /NDL >nul
robocopy Output backups\%name%\Output /NFL /NDL >nul
copy Raport_Smith.html backups\%name%\Raport_Smith.html
echo Kopia zapasowa zostala utworzona w katalogu backups\%name%.
pause
goto menu

:exit
echo Wybrales wyjscie
pause
exit
