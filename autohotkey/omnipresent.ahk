#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


;Make capslock harder to hit (requires a shift press, otherwise it's just a control key)
+Capslock::Capslock
Capslock::Control


;Altium Designer keybinds
F1::
WinGetTitle, Title, A
;MsgBox, The active window is "%Title%".
IfInString, Title, Altium Designer
{
  ;MsgBox, We're in Altium.
  SendInput v
  Sleep 100
  SendInput w
  Sleep 100
  SendInput s
  Sleep 100
  SendInput u
}
return

