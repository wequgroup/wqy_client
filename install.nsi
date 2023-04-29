; 该脚本使用 HM VNISEdit 脚本编辑器向导产生

; 安装程序初始定义常量
!define PRODUCT_NAME "WeDuck"
!define PRODUCT_VERSION "1000"
!define PRODUCT_PUBLISHER "微趣奈特"
!define PRODUCT_WEB_SITE "https://wequ.net"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\WeDuck.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "pyapp\icon\logo.ico"
!define MUI_UNICON "pyapp\icon\logo.ico"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
!insertmacro MUI_PAGE_LICENSE "licence.txt"
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_SHOWREADME
!define MUI_FINISHPAGE_SHOWREADME_Function AutoBoot
!define MUI_FINISHPAGE_SHOWREADME_TEXT "添加开机启动"
!define MUI_FINISHPAGE_RUN "$INSTDIR\WeDuck.exe"
!insertmacro MUI_PAGE_FINISH

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "WeDuckInstall.exe"
InstallDir "$PROGRAMFILES\WeDuck"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "微趣鸭"

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File /r "build\WeDuck\*.*"
  CreateDirectory "$SMPROGRAMS\WeDuck"
  CreateShortCut "$SMPROGRAMS\WeDuck\WeDuck.lnk" "$INSTDIR\WeDuck.exe"
  CreateShortCut "$DESKTOP\WeDuck.lnk" "$INSTDIR\WeDuck.exe"
  File "build\WeDuck\WeDuck.exe"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\WeDuck\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\WeDuck\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\WeDuck.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\WeDuck.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  以下是安装程序的卸载部分  *
 ******************************/

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\WeDuck.exe"
  
  Delete "$INSTDIR\*.pyd"
  Delete "$INSTDIR\*.dll"
  Delete "$INSTDIR\*.zip"

  Delete "$SMPROGRAMS\WeDuck\Uninstall.lnk"
  Delete "$SMPROGRAMS\WeDuck\Website.lnk"
  Delete "$DESKTOP\WeDuck.lnk"
  Delete "$SMPROGRAMS\WeDuck\WeDuck.lnk"

  RMDir "$SMPROGRAMS\WeDuck"

  RMDir /r "$INSTDIR\WeDuck.exe.WebView2"
  RMDir /r "$INSTDIR\webview"
  RMDir /r "$INSTDIR\psutil"
  RMDir /r "$INSTDIR\web"
  RMDir /r "$INSTDIR\static"
  RMDir /r "$INSTDIR\pythonnet"
  RMDir /r "$INSTDIR\PIL"
  RMDir /r "$INSTDIR\markupsafe"
  RMDir /r "$INSTDIR\importlib_metadata-6.6.0.dist-info"
  RMDir /r "$INSTDIR\greenlet"
  RMDir /r "$INSTDIR\clr_loader"
  RMDir /r "$INSTDIR\clr_loader"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd

#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要完全移除 $(^Name) ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从您的计算机移除。"
FunctionEnd

Function AutoBoot
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "WeDuck" "$INSTDIR\WeDuck.exe --mini yes"
FunctionEnd
