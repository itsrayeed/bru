##    pygame - Python Game Library
##    Copyright (C) 2000-2003  Pete Shinners
##
##    This library is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.
##
##    This library is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Library General Public License for more details.
##
##    You should have received a copy of the GNU Library General Public
##    License along with this library; if not, write to the Free
##    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##
##    Pete Shinners
##    pete@shinners.org

"sysfont, used in the font module to find system fonts"

import os, sys

#Python 3 compatibility
try:
    bytes
except NameError:
    def toascii(raw):
        return raw.decode('ascii', 'ignore').encode('ascii')
else:
    def toascii(raw):
        return raw.decode('ascii', 'ignore')

#create simple version of the font name
def _simplename(name):
    return ''.join([c.lower() for c in name if c.isalnum()])


#insert a font and style into the font dictionary
def _addfont(name, bold, italic, font, fontdict):
    if name not in fontdict:
        fontdict[name] = {}
    fontdict[name][bold, italic] = font


#read the fonts on windows
# Info taken from:
# http://www.microsoft.com/typography/fonts/winxp.htm
# with extra files added from:
# <fill this in>
# File name, family, (Bold, Italic)
XP_default_font_files = [
    ('ahronbd.ttf', 'Aharoni', (True, False)),
    ('andlso.ttf', 'Andalus', (False, False)),
    ('angsa.ttf', 'Angsana New', (False, False)),
    ('angsab.ttf', 'Angsana New', (True, False)),
    ('angsai.ttf', 'Angsana New', (False, True)),
    ('angsaz.ttf', 'Angsana New', (True, True)),
    ('angsau.ttf', 'AngsanaUPC', (False, False)),
    ('angsaub.ttf', 'AngsanaUPC', (True, False)),
    ('angsaui.ttf', 'AngsanaUPC', (False, True)),
    ('angsauz.ttf', 'AngsanaUPC', (True, True)),
    ('artro.ttf', 'Arabic Transparent', (False, False)),
    ('artrbdo.ttf', 'Arabic Transparent', (True, False)),
    ('agatha.ttf', 'Agatha', (False, False)),
    ('arial.ttf', 'Arial', (False, False)),
    ('arialbd.ttf', 'Arial', (True, False)),
    ('ariali.ttf', 'Arial', (False, True)),
    ('arialbi.ttf', 'Arial', (True, True)),
    ('ariblk.ttf', 'Arial Black', (False, False)),
    ('browa.ttf', 'Browallia New', (False, False)),
    ('browab.ttf', 'Browallia New', (True, False)),
    ('browai.ttf', 'Browallia New', (False, True)),
    ('browaz.ttf', 'Browallia New', (True, True)),
    ('browau.ttf', 'BrowalliaUPC', (False, False)),
    ('browaub.ttf', 'BrowalliaUPC', (True, False)),
    ('browaui.ttf', 'BrowalliaUPC', (False, True)),
    ('browauz.ttf', 'BrowalliaUPC', (True, True)),
    ('comic.ttf', 'Comic Sans MS', (False, False)),
    ('comicbd.ttf', 'Comic Sans MS', (True, False)),
    ('cordia.ttf', 'Cordia New', (False, False)),
    ('cordiab.ttf', 'Cordia New', (True, False)),
    ('cordiai.ttf', 'Cordia New', (False, True)),
    ('cordiaz.ttf', 'Cordia New', (True, True)),
    ('cordiau.ttf', 'CordiaUPC', (False, False)),
    ('cordiaub.ttf', 'CordiaUPC', (True, False)),
    ('cordiaui.ttf', 'CordiaUPC', (False, True)),
    ('cordiauz.ttf', 'CordiaUPC', (True, True)),
    ('cour.ttf', 'Courier New', (False, False)),
    ('courbd.ttf', 'Courier New', (True, False)),
    ('couri.ttf', 'Courier New', (False, True)),
    ('courbi.ttf', 'Courier New', (True, True)),
    ('david.ttf', 'David', (False, False)),
    ('davidbd.ttf', 'David', (True, False)),
    ('davidtr.ttf', 'David Transparent', (False, False)),
    ('upcdl.ttf', 'DilleniaUPC', (False, False)),
    ('upcdb.ttf', 'DilleniaUPC', (True, False)),
    ('upcdi.ttf', 'DilleniaUPC', (False, True)),
    ('upcdbi.ttf', 'DilleniaUPC', (True, True)),
    ('estre.ttf', 'Estrangelo Edessa', (False, False)),
    ('upcel.ttf', 'EucrosialUPC', (False, False)),
    ('upceb.ttf', 'EucrosialUPC', (True, False)),
    ('upcei.ttf', 'EucrosialUPC', (False, True)),
    ('upcebi.ttf', 'EucrosialUPC', (True, True)),
    ('mriamfx.ttf', 'Fixed Miriam Transparent', (False, False)),
    ('framd.ttf', 'Franklin Gothic Medium', (False, False)),
    ('framdit.ttf', 'Franklin Gothic Medium', (False, True)),
    ('frank.ttf', 'FrankRuehl', (False, False)),
    ('upcfl.ttf', 'FreesialUPC', (False, False)),
    ('upcfb.ttf', 'FreesialUPC', (True, False)),
    ('upcfi.ttf', 'FreesialUPC', (False, True)),
    ('upcfbi.ttf', 'FreesialUPC', (True, True)),
    ('gautami.ttf', 'Gautami', (False, False)),
    ('georgia.ttf', 'Georgia', (False, False)),
    ('georgiab.ttf', 'Georgia', (True, False)),
    ('georgiai.ttf', 'Georgia', (False, True)),
    ('georgiaz.ttf', 'Georgia', (True, True)),
    ('impact.ttf', 'Impact', (False, False)),
    ('upcil.ttf', 'IrisUPC', (False, False)),
    ('upcib.ttf', 'IrisUPC', (True, False)),
    ('upcii.ttf', 'IrisUPC', (False, True)),
    ('upcibi.ttf', 'IrisUPC', (True, True)),
    ('upcjl.ttf', 'JasmineUPC', (False, False)),
    ('upcjb.ttf', 'JasmineUPC', (True, False)),
    ('upcji.ttf', 'JasmineUPC', (False, True)),
    ('upcjbi.ttf', 'JasmineUPC', (True, True)),
    ('upckl.ttf', 'KodchiangUPC', (False, False)),
    ('upckb.ttf', 'KodchiangUPC', (True, False)),
    ('upcki.ttf', 'KodchiangUPC', (False, True)),
    ('upckbi.ttf', 'KodchiangUPC', (True, True)),
    ('latha.ttf', 'Latha', (False, False)),
    ('lvnm.ttf', 'Levenim MT', (False, False)),
    ('lvnmbd.ttf', 'Levenim MT', (True, False)),
    ('upcll.ttf', 'LilyUPC', (False, False)),
    ('upclb.ttf', 'LilyUPC', (True, False)),
    ('upcli.ttf', 'LilyUPC', (False, True)),
    ('upclbi.ttf', 'LilyUPC', (True, True)),
    ('lucon.ttf', 'Lucida Console', (False, False)),
    ('l_10646.ttf', 'Lucida Sans Unicode', (False, False)),
    ('mangal.ttf', 'Mangal', (False, False)),
    ('marlett.ttf', 'Marlett', (False, False)),
    ('micross.ttf', 'Microsoft Sans Serif', (False, False)),
    ('mriam.ttf', 'Miriam', (False, False)),
    ('mriamc.ttf', 'Miriam Fixed', (False, False)),
    ('mriamtr.ttf', 'Miriam Transparent', (False, False)),
    ('mvboli.ttf', 'MV Boli', (False, False)),
    ('nrkis.ttf', 'Narkisim', (False, False)),
    ('pala.ttf', 'Falatino Linotype', (False, False)),
    ('palab.ttf', 'Falatino Linotype', (True, False)),
    ('palai.ttf', 'Falatino Linotype', (False, True)),
    ('palabi.ttf', 'Falatino Linotype', (True, True)),
    ('raavi.ttf', 'Raavi', (False, False)),
    ('rod.ttf', 'Rod', (False, False)),
    ('rodtr.ttf', 'Rod Transparent', (False, False)),
    ('shruti.ttf', 'Shruti', (False, False)),
    ('simpo.ttf', 'Simplified Arabic', (False, False)),
    ('simpbdo.ttf', 'Simplified Arabic', (True, False)),
    ('simpfxo.ttf', 'Simplified Arabic Fixed', (False, False)),
    ('sylfaen.ttf', 'Sylfaen', (False, False)),
    ('symbol.ttf', 'Symbol', (False, False)),
    ('tahoma.ttf', 'Tahoma', (False, False)),
    ('tahomabd.ttf', 'Tahoma', (True, False)),
    ('times.ttf', 'Times New Roman', (False, False)),
    ('timesbd.ttf', 'Times New Roman', (True, False)),
    ('timesi.ttf', 'Times New Roman', (False, True)),
    ('timesbi.ttf', 'Times New Roman', (True, True)),
    ('trado.ttf', 'Traditional Arabic', (False, False)),
    ('tradbdo.ttf', 'Traditional Arabic', (True, False)),
    ('Trebuc.ttf', 'Trebuchet MS', (False, False)),
    ('Trebucbd.ttf', 'Trebuchet MS', (True, False)),
    ('Trebucit.ttf', 'Trebuchet MS', (False, True)),
    ('Trebucbi.ttf', 'Trebuchet MS', (True, True)),
    ('tunga.ttf', 'Tunga', (False, False)),
    ('verdana.ttf', 'Verdana', (False, False)),
    ('verdanab.ttf', 'Verdana', (True, False)),
    ('verdanai.ttf', 'Verdana', (False, True)),
    ('verdanaz.ttf', 'Verdana', (True, True)),
    ('webdings.ttf', 'Webdings', (False, False)),
    ('wingding.ttf', 'Wingdings', (False, False)),
    ('simhei.ttf', 'SimHei', (False, False)),
    ('simfang.ttf', 'FangSong_GB2312', (False, False)),
    ('kaiu.ttf', 'DFKai-SB', (False, False)),
    ('simkai.ttf', 'KaiTi_GB2312', (False, False)),
    ('msgothic.ttc', 'MS Gothic', (False, False)),
    ('msmincho.ttc', 'MS Mincho', (False, False)),
    ('gulim.ttc', 'Gulim', (False, False)),
    ('mingliu.ttc', 'Mingliu', (False, False)),
    ('simsun.ttc', 'Simsun', (False, False)),
    ('batang.ttc', 'Batang', (False, False)),
    ]

def initsysfonts_win32():
    try:
        import _winreg
    except ImportError:
        import winreg as _winreg
    fonts = {}
    mods = 'demibold', 'narrow', 'light', 'unicode', 'bt', 'mt'
    fontdir = os.path.join(os.environ['WINDIR'], "Fonts")

    #this is a list of registry keys containing information
    #about fonts installed on the system.
    keys = []

    #add recognized fonts from the fonts directory because the default
    #fonts may not be entered in the registry.
    win_font_files_mapping = dict(
        [(font.lower(), (_simplename(name), face))
         for font, name, face in XP_default_font_files])

    font_dir_path = os.path.join(os.environ['windir'], 'fonts')
    try:
        font_file_paths = glob.glob(os.path.join(font_dir_path, '*.tt?'))
    except Exception:
        pass
    else:
        for font in font_file_paths:
            file_name = os.path.basename(font)
            try:
                name, face = win_font_file_mapping[file_name]
            except KeyError:
                pass
            else:
                try:
                    faces = fonts[name]
                except KeyError:
                    _addfont(name, face[0], face[1], font, fonts)
                else:
                    if face not in faces:
                        _addfont(name, face[0], face[1], font, fonts)

    #add additional fonts entered in the registry.

    #find valid registry keys containing font information.
    possible_keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Fonts",
        r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts",
        r"SOFTWARE\Microsoft\Windows[NT]\CurrentVersion\Fonts",
        ]

    for key_name in possible_keys:
        try:
            key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, key_name)
            keys.append(key)
        except WindowsError:
            pass

    for key in keys:
        fontdict = {}
        for i in range(_winreg.QueryInfoKey(key)[1]):
            try: name, font, t = _winreg.EnumValue(key,i)
            except EnvironmentError: break

            # try and handle windows unicode strings for some file names.
            
            # here are two documents with some information about it:
            # http://www.python.org/peps/pep-0277.html
            # https://www.microsoft.com/technet/archive/interopmigration/linux/mvc/lintowin.mspx#ECAA
            try:
                font = str(font)
            except UnicodeEncodeError:
                # MBCS is the windows encoding for unicode file names.
                try:
                    font = font.encode('MBCS')
                except:
                    # no goodness with str or MBCS encoding... skip this font.
                    continue
   
            if font[-4:].lower() not in [".ttf", ".ttc"]:
                continue
            if os.sep not in font:
                font = os.path.join(fontdir, font)

            if name[-10:] == '(TrueType)':
                name = name[:-11]
            name = name.lower().split()

            bold = italic = 0
            for m in mods:
                if m in name:
                    name.remove(m)
            if 'bold' in name:
                name.remove('bold')
                bold = 1
            if 'italic' in name:
                name.remove('italic')
                italic = 1
            name = ''.join(name)

            name=_simplename(name)

            _addfont(name, bold, italic, font, fonts)

    return fonts


#read of the fonts on osx (fill me in!)
def initsysfonts_darwin():
    # if the X11 binary exists... try and use that.
    #  TODO: Not likely to be there on pre 10.4.x ...
    #    so still need to do other OSX specific method.
    if os.path.exists("/usr/X11/bin/fc-list"):
        return initsysfonts_unix()

    paths = ['/Library/Fonts',
             '~/Library/Fonts',
             '/Local/Library/Fonts',
             '/Network/Library/Fonts']
    fonts = {}
    for p in paths:
        if os.path.isdir(p):
            pass
            #os.path.walk(p, _fontwalk, fonts)
    return fonts




#read the fonts on unix
def initsysfonts_unix():
    import subprocess

    fonts = {}

    # we use the fc-list from fontconfig to get a list of fonts.

    try:
        # note, we capture stderr so if fc-list isn't there to stop stderr printing.
        flout, flerr = subprocess.Popen('fc-list : file family style', shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        close_fds=True).communicate()
    except Exception:
        return fonts

    entries = toascii(flout)
    try:
        for line in entries.split('\n'):
            try:
                filename, family, style = line.split(':', 2)
                if filename[-4:].lower() in ['.ttf', '.ttc']:
                    bold = style.find('Bold') >= 0
                    italic = style.find('Italic') >= 0
                    oblique = style.find('Oblique') >= 0
                    for name in family.split(','):
                        if name:
                            break
                    else:
                        name = os.path.splitext(os.path.basename(filename))[0]
                    _addfont(_simplename(name),
                             bold, italic or oblique, filename, fonts)
            except Exception:
                # try the next one.
                pass
    except Exception:
        pass

    return fonts



#create alias entries
def create_aliases():
    aliases = (
        ('monospace', 'misc-fixed', 'courier', 'couriernew', 'console',
                'fixed', 'mono', 'freemono', 'bitstreamverasansmono',
                'verasansmono', 'monotype', 'lucidaconsole'),
        ('sans', 'arial', 'helvetica', 'swiss', 'freesans',
                'bitstreamverasans', 'verasans', 'verdana', 'tahoma'),
        ('serif', 'times', 'freeserif', 'bitstreamveraserif', 'roman',
                'timesroman', 'timesnewroman', 'dutch', 'veraserif',
                'georgia'),
        ('wingdings', 'wingbats'),
    )
    for set in aliases:
        found = None
        fname = None
        for name in set:
            if name in Sysfonts:
                found = Sysfonts[name]
                fname = name
                break
        if not found:
            continue
        for name in set:
            if name not in Sysfonts:
                Sysalias[name] = found


Sysfonts = {}
Sysalias = {}

#initialize it all, called once
def initsysfonts():
    if sys.platform == 'win32':
        fonts = initsysfonts_win32()
    elif sys.platform == 'darwin':
        fonts = initsysfonts_darwin()
    else:
        fonts = initsysfonts_unix()
    Sysfonts.update(fonts)
    create_aliases()
    if not Sysfonts: #dummy so we don't try to reinit
        Sysfonts[None] = None



#the exported functions

def SysFont(name, size, bold=False, italic=False):
    """pygame.font.SysFont(name, size, bold=False, italic=False) -> Font
       create a pygame Font from system font resources

       This will search the system fonts for the given font
       name. You can also enable bold or italic styles, and
       the appropriate system font will be selected if available.

       This will always return a valid Font object, and will
       fallback on the builtin pygame font if the given font
       is not found.

       Name can also be a comma separated list of names, in
       which case set of names will be searched in order. Pygame
       uses a small set of common font aliases, if the specific
       font you ask for is not available, a reasonable alternative
       may be used.
    """
    import pygame.font

    if not Sysfonts:
        initsysfonts()
    
    gotbold = gotitalic = False
    fontname = None
    if name:
        allnames = name
        for name in allnames.split(','):
            name = _simplename(name)
            styles = Sysfonts.get(name)
            if not styles:
                styles = Sysalias.get(name)
            if styles:
                while not fontname:
                    plainname = styles.get((False, False))
                    fontname = styles.get((bold, italic))
                    if not fontname:
                        fontname = plainname
                    elif plainname != fontname:
                        gotbold = bold
                        gotitalic = italic
            if fontname: break

    font = pygame.font.Font(fontname, size)
    if bold and not gotbold:
        font.set_bold(1)
    if italic and not gotitalic:
        font.set_italic(1)

    return font


def get_fonts():
    """pygame.font.get_fonts() -> list
       get a list of system font names

       Returns the list of all found system fonts. Note that
       the names of the fonts will be all lowercase with spaces
       removed. This is how pygame internally stores the font
       names for matching.
    """
    if not Sysfonts:
        initsysfonts()
    return list(Sysfonts.keys())


def match_font(name, bold=0, italic=0):
    """pygame.font.match_font(name, bold=0, italic=0) -> name
       find the filename for the named system font

       This performs the same font search as the SysFont()
       function, only it returns the path to the TTF file
       that would be loaded. The font name can be a comma
       separated list of font names to try.

       If no match is found, None is returned.
    """
    if not Sysfonts:
        initsysfonts()

    fontname = None
    allnames = name
    for name in allnames.split(','):
        name = _simplename(name)
        styles = Sysfonts.get(name)
        if not styles:
            styles = Sysalias.get(name)
        if styles:
            while not fontname:
                fontname = styles.get((bold, italic))
                if italic:
                    italic = 0
                elif bold:
                    bold = 0
                elif not fontname:
                    fontname = list(styles.values())[0]
        if fontname: break
    return fontname


