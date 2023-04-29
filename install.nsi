; �ýű�ʹ�� HM VNISEdit �ű��༭���򵼲���

; ��װ�����ʼ���峣��
!define PRODUCT_NAME "WeDuck"
!define PRODUCT_VERSION "1000"
!define PRODUCT_PUBLISHER "΢Ȥ����"
!define PRODUCT_WEB_SITE "https://wequ.net"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\WeDuck.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; ------ MUI �ִ����涨�� (1.67 �汾���ϼ���) ------
!include "MUI.nsh"

; MUI Ԥ���峣��
!define MUI_ABORTWARNING
!define MUI_ICON "pyapp\icon\logo.ico"
!define MUI_UNICON "pyapp\icon\logo.ico"

; ��ӭҳ��
!insertmacro MUI_PAGE_WELCOME
; ���Э��ҳ��
!insertmacro MUI_PAGE_LICENSE "licence.txt"
; ��װĿ¼ѡ��ҳ��
!insertmacro MUI_PAGE_DIRECTORY
; ��װ����ҳ��
!insertmacro MUI_PAGE_INSTFILES
; ��װ���ҳ��
!define MUI_FINISHPAGE_SHOWREADME
!define MUI_FINISHPAGE_SHOWREADME_Function AutoBoot
!define MUI_FINISHPAGE_SHOWREADME_TEXT "��ӿ�������"
!define MUI_FINISHPAGE_RUN "$INSTDIR\WeDuck.exe"
!insertmacro MUI_PAGE_FINISH

; ��װж�ع���ҳ��
!insertmacro MUI_UNPAGE_INSTFILES

; ��װ�����������������
!insertmacro MUI_LANGUAGE "SimpChinese"

; ��װԤ�ͷ��ļ�
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI �ִ����涨����� ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "WeDuckInstall.exe"
InstallDir "$PROGRAMFILES\WeDuck"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "΢ȤѼ"

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
 *  �����ǰ�װ�����ж�ز���  *
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

#-- ���� NSIS �ű��༭�������� Function ���α�������� Section ����֮���д���Ա��ⰲװ�������δ��Ԥ֪�����⡣--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "��ȷʵҪ��ȫ�Ƴ� $(^Name) ���������е������" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) �ѳɹ��ش����ļ�����Ƴ���"
FunctionEnd

Function AutoBoot
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "WeDuck" "$INSTDIR\WeDuck.exe --mini yes"
FunctionEnd
