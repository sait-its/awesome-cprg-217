import win32api


def main():
    # Frequency (in Hertz) and duration (in milliseconds)
    frequency = 1000  # 1000 Hz
    duration = 500  # 0.5 second
    # Call Beep
    win32api.Beep(frequency, duration)


if __name__ == "__main__":
    main()
