import ctypes


def get_ppi():
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    #print("Horizontal DPI is", windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX))
    #print("Vertical DPI is", windll.gdi32.GetDeviceCaps(dc, LOGPIXELSY))
    user32.ReleaseDC(0, dc)
    return pix_per_inch


def window_scaler():
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    return ScaleFactor
