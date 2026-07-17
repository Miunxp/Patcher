from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

from ApkPatcher.Utils.Files_Check import __version__


Tag = f"\n{C.CC}————|———————|————{C.G}•❀ {C.OG}Tag {C.G}❀•{C.CC}————|———————|————\n"

FE = f"{C.P}\n   |\n   ╰{C.CC}┈{C.OG}➢ {C.G}ApkPatcher"

EX = f"{FE} -i Your_Apk_Path.apk {C.OG}"


class CustomArgumentParser(M.argparse.ArgumentParser):
    # ---------------- Error Handling ----------------
    def error(self, message):
        suggestion = ""
        for action in self._actions:
            if action.option_strings and any(option in message for option in action.option_strings):
                if action.dest == 'input':
                    suggestion = (
                        f'\n{C.FYI}{C.G} ตรวจสอบให้แน่ใจว่า "ไม่มีการเว้นวรรคเกิน" ในชื่อโฟลเดอร์หรือไฟล์ APK ที่ระบุในข้อความนำเข้า หากมี ให้ลบช่องว่างออกหรือตั้งชื่อใหม่ให้ถูกต้อง\n\n'
                        f'\n{C.INFO} การใช้พารามิเตอร์ใบรับรอง (Certificate Flag): {C.OG}-c {C.P}( ระบุพาธไฟล์ pem/crt/cert ){EX}-c {C.Y}certificate.cert\n\n'
                        f'\n{C.INFO} หากคุณกำลังใช้งานบนโปรแกรมจำลอง (Emulator) ในคอมพิวเตอร์ ให้ใช้พารามิเตอร์: {C.OG}-e{EX}-c {C.Y}certificate.cert {C.OG}-e\n'
                    )

                elif action.dest == 'Merge':
                    suggestion = (
                        f'\n{C.INFO} สำหรับการรวมไฟล์ APK (Merge) เท่านั้น\n\n'
                        f'\n{C.INFO} นามสกุลไฟล์ที่รองรับสำหรับการรวมไฟล์ {C.Y}( .apks/.xapk/.apkm )'
                        f'\n{FE}{C.OG} -m {C.G}Your_Apk_Path.apks\n'
                    )

                break

        exit(
            f'\n{C.ERROR} ข้อผิดพลาด: {message}\n'
            f'\n{suggestion}'
        )

    # ---------------- Print Help ----------------
    def print_help(self):

        super().print_help()

        print(f"\n{C.INFO} แพตช์เริ่มต้นของ ApkPatcher คือการบายพาส VPN & SSL หากต้องการดูรายการพารามิเตอร์แพตช์อื่นๆ ให้ใช้คำสั่ง: {C.G}ApkPatcher -O{C.C}\n")

    # ---------------- Other Patch ----------------
    def Other_Patch(self):
        print(
            f"""\n{C.X}{C.C} คำแนะนำการใช้งานพารามิเตอร์แพตช์อื่นๆ (กรุณาเรียงลำดับพารามิเตอร์ให้ถูกต้อง)

 <พารามิเตอร์>                 {C.G}─•❀•❀ {C.C}ข้อมูลการแพตช์ {C.G}❀•❀•─ {C.OG}

  -A, {C.C}--AES_Logs        {C.Y} -> {C.G}ฝังการบันทึกบันทึก AES (AES Logs Inject) {C.OG}
  -A2, {C.C}--Algorithm      {C.Y} -> {C.G}ฝังการบันทึกบันทึกอัลกอริทึม (Algorithm Logs Inject) {C.OG}
  -D, {C.C}--Android_ID      {C.Y} -> {C.G}ฮุก Android ID เพื่อบายพาสการล็อกอินหนึ่งเครื่องต่อหนึ่งบัญชี {C.OG}
  -f, {C.C}--Flutter         {C.Y} -> {C.G}บายพาส Flutter SSL {C.OG}
  -l, {C.C}--Load_Modules    {C.Y} -> {C.G}พาธของโมดูล Xposed & LSP {C.P}( ปัจจุบันยังไม่รองรับโมดูล XSharedPreferences ) {C.OG}
  -p, {C.C}--Pairip          {C.Y} -> {C.G}บายพาส Pairip CERT SSL {C.OG}
  -P, {C.C}--Purchase        {C.Y} -> {C.G}บายพาสการซื้ออินแอป / ระบบชำระเงิน / ราคา {C.OG}
  -r, {C.C}--Random_Info     {C.Y} -> {C.G}จำลองข้อมูลอุปกรณ์ (ปลอมรุ่นมือถือ) {C.OG}
  -rmads, {C.C}--Remove_Ads  {C.Y} -> {C.G}บายพาสและโฆษณาออก {C.OG}
  -rmss, {C.C}--Remove_SS    {C.Y} -> {C.G}บายพาสการจำกัดการจับภาพหน้าจอ {C.OG}
  -rmusb, {C.C}--Remove_USB  {C.Y} -> {C.G}บายพาสการตรวจจับการดีบัก USB {C.OG}
  -pkg, {C.C}--Spoof_PKG     {C.Y} -> {C.G}ปลอมแปลงการตรวจจับชื่อแพ็กเกจ (Spoof Package) {C.OG}
  -pine, {C.C}--Pine_Hook    {C.Y} -> {C.G}การฮุกด้วย Pine Hook {C.OG}
  -skip {C.C}[Skip_Patch ...]{C.Y} -> {C.G}ข้ามขั้นตอนการแพตช์ที่ระบุ {C.P}( เช่น getAcceptedIssuers ) {C.OG}
  -s, {C.C}--AES_S           {C.Y} -> {C.G}คุณต้องการแยกไฟล์ AES.smali Dex ออกมาต่างหากหรือไม่ {C.OG}
  -t, {C.C}--TG_Patch        {C.Y} -> {C.G}แพตช์สำหรับ Telegram / Plus Patcher {C.OG}
  -x, {C.C}--Hook_CoreX      {C.Y} -> {C.G}พารามิเตอร์ฮุก CoreX: {C.OG}-p -x {C.P}( รองรับเฉพาะ [ arm64 ] เท่านั้น )"""
        )

        user_input = input(f"\n\n{C.B}[ {C.P}* {C.B}] {C.C} ต้องการดูตัวอย่างการใช้งานหรือไม่?\n{C.G}  |\n  └──── {C.CC}~ พิมพ์ y เพื่อดู / หรือกด Enter เพื่อออก {C.G}$ : {C.Y}")

        if user_input.lower() == "y":
            print(
                f"""\n{Tag.replace("Tag", "AES Logs Inject")}

{C.INFO} พารามิเตอร์ฝังบันทึกบันทึก AES MT Logs: {C.OG}-A{EX}-A


{C.INFO} หากต้องการแยกไฟล์ AES.smali Dex ให้ใช้พารามิเตอร์: {C.OG}-A -s{EX}-A -s


{C.INFO} พารามิเตอร์ฝังบันทึกบันทึกอัลกอริทึม: {C.OG}-A2{EX}-A2

{Tag.replace("Tag", "Hook Android ID")}

{C.INFO} ฮุก Android ID เพื่อบายพาสการล็อกอินจำกัดอุปกรณ์ ให้ใช้พารามิเตอร์: {C.OG}-D {C.P}( ใส่เลข Android ID 16 หลักของเครื่องคุณ ){EX}-D {C.Y}7e9f51f096bd5c83

{Tag.replace("Tag", "isFlutter / isPairip")}

{C.INFO} หากไฟล์ APK เป็น Flutter ให้ใช้พารามิเตอร์เพิ่มเติม: {C.OG}-f{EX}-f


{C.INFO} หากไฟล์ APK เป็น Pairip ให้ใช้พารามิเตอร์เพิ่มเติม: {C.OG}-p {C.P}( ไฟล์ APK ที่ได้จะไม่เซ็นชื่อ ต้องติดตั้งใน VM / Multi_App เท่านั้น ){EX}-p


{C.INFO} หากไฟล์ APK เป็น Pairip และต้องการฮุก CoreX ให้ใช้พารามิเตอร์เพิ่มเติม: {C.OG}-p -x {C.P}( ติดตั้งได้โดยตรง รองรับเฉพาะ [ arm64 ] ){EX}-p -x

{Tag.replace("Tag", "Spoof PKG / Device Info")}

{C.INFO} พารามิเตอร์ปลอมแปลงชื่อแพ็กเกจ (Spoof Package): {C.OG}-pkg {C.P}( Dex / Manifest / Res ){EX}-pkg

{C.INFO} พารามิเตอร์จำลองข้อมูลอุปกรณ์: {C.OG}-r{EX}-r


{C.INFO} ใช้งานร่วมกับพารามิเตอร์ Android ID: {C.OG}-r -D {C.P}( กำหนดเลข Android ID 16 หลักของคุณเอง ){EX}-r -D {C.Y}7e9f51f096bd5c83

{Tag.replace("Tag", "Pine Hook")}

{C.INFO} พารามิเตอร์ Pine Hook: {C.OG}-pine -l {C.P}( ระบุพาธไฟล์โมดูล Xposed หรือ LSP ){EX}-pine -l {C.Y}NoVPNDetect.apk just.trust.me.apk

{Tag.replace("Tag", "Bypass Ads / SS / USB")}

{C.INFO} พารามิเตอร์ข้ามโฆษณา (Bypass Ads): {C.OG}-rmads{EX}-rmads


{C.INFO} พารามิเตอร์ปลดล็อกการจำกัดจับภาพหน้าจอ: {C.OG}-rmss{EX}-rmss


{C.INFO} พารามิเตอร์บายพาสการตรวจจับดีบัก USB: {C.OG}-rmusb{EX}-rmusb

{Tag.replace("Tag", "isPurchase / Skip Patch")}

{C.INFO} พารามิเตอร์บายพาสระบบซื้อของในแอป (Purchase / Paid / Price): {C.OG}-P{EX}-P


{C.INFO} พารามิเตอร์ข้ามการแพตช์เฉพาะจุด: {C.OG}-skip{EX}-skip {C.Y}getAcceptedIssuers

{Tag.replace("Tag", "Telegram / Plus Patch")}

{C.INFO} พารามิเตอร์สำหรับแพตช์ Telegram / Plus: {C.OG}-t{EX}-t\n"""
            )

        else:
            return


# ---------------- Parse Arguments ----------------
def parse_arguments():

    args = M.sys.argv[1:]

    if '-O' in args:
        exit(CustomArgumentParser().Other_Patch())

    if any(arg.startswith('-') for arg in args):
        parser = CustomArgumentParser(description=f'{C.C}ApkPatcher เวอร์ชัน v{__version__}')
    else:
        parser = M.argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '-i',
        dest='input',
        help=f'{C.Y}->{C.G} ระบุพาธไฟล์ APK ขาเข้า...{C.C}'
    )

    group.add_argument(
        '-m',
        dest='Merge',
        help=f'{C.Y}->{C.G} Anti-Split (สำหรับการรวมไฟล์ APK เท่านั้น){C.C}'
    )

    group.add_argument(
        '-C',
        dest='Credits',
        action='store_true',
        help=f'{C.Y}->{C.G} แสดงเครดิตผู้พัฒนา{C.C}'
    )

    additional = parser.add_argument_group(f'{C.OG}[ * ] พารามิเตอร์เพิ่มเติม (Additional Flags){C.C}')

    additional.add_argument(
        '-a',
        '--APKEditor',
        action='store_true',
        help=f'{C.Y}-> {C.G}ใช้งาน APKEditor (ค่าเริ่มต้นจะเป็น APKTool){C.C}'
    )

    additional.add_argument(
        '-e',
        '--For_Emulator',
        action='store_true',
        help=f'{C.Y}->{C.G} หากใช้งานบนโปรแกรมจำลอง (Emulator) ในคอมพิวเตอร์ ให้เปิดใช้งานพารามิเตอร์ -e{C.C}'
    )

    additional.add_argument(
        '-c',
        dest='CA_Certificate',
        type=str,
        nargs='*',
        help=f"{C.Y}->{C.G} ระบุไฟล์ CA-Certificate ของแอปดักจับแพ็กเก็ต เช่น HttpCanary / Reqable / ProxyPin เป็นต้น{C.C}"
    )

    additional.add_argument(
        '-u',
        dest='unsigned_apk',
        action='store_true',
        help=f"{C.Y}->{C.G} คงสถานะไฟล์ APK แบบไม่เซ็นชื่อ (Unsigned){C.C}"
    )


    # ---------------- Other Patch Flags ----------------
    parser.add_argument(
        '-A',
        '--AES_Logs',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-A2',
        '--Algorithm',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-D',
        '--Android_ID',
        type=str,
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-f',
        '--Flutter',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-l',
        '--Load_Modules',
        type=str,
        nargs='*',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-p',
        '--Pairip',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-P',
        '--Purchase',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-r',
        '--Random_Info',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-rmads',
        '--Remove_Ads',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-rmss',
        '--Remove_SS',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-rmusb',
        '--Remove_USB',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-pkg',
        '--Spoof_PKG',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-pine',
        '--Pine_Hook',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-skip',
        dest='Skip_Patch',
        nargs='*',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-s',
        '--AES_S',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-t',
        '--TG_Patch',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-x',
        '--Hook_CoreX',
        action='store_true',
        help=M.argparse.SUPPRESS
    )


    Ext = ('.apk', '.apks', '.apkm', '.xapk')

    fixed = []; start = None; Valid_Ext = False

    for index, option in enumerate(args):
        if option in ['-i', '-m', '-C']:
            start, fixed = index + 1, fixed + [option]
        elif start and (option.endswith(Ext) or M.os.path.isdir(option)):
            fixed, start = fixed + [' '.join(args[start:index+1])], None
            Valid_Ext = True
        elif not start:
            fixed.append(option)


    if not Valid_Ext and M.sys.argv[1:2] != ['-C']:
        print(f"\n{C.X}{C.C} รองรับเฉพาะไฟล์นามสกุลต่อไปนี้เท่านั้น: {C.G}{Ext}\n")

    print(f"\n{C.S} พาธนำเข้า (Input Path) {C.E} {C.OG}->❥{C.Y}", *fixed, f"{C.CC}\n")

    return parser.parse_args(fixed)