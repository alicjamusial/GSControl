tasks = [
    [tc.SetBuiltinDetumblingBlockMaskTelecommand(1, 255), Send, WaitMode.NoWait],
    [2, Sleep, WaitMode.NoWait],
    [tc.SetBuiltinDetumblingBlockMaskTelecommand(2, 255), Send, WaitMode.NoWait],
    [2, Sleep, WaitMode.NoWait],
    [tc.SetBuiltinDetumblingBlockMaskTelecommand(3, 255), Send, WaitMode.NoWait],
    [2, Sleep, WaitMode.NoWait],
    [tc.SetBuiltinDetumblingBlockMaskTelecommand(4, 0), Send, WaitMode.NoWait],
    [2, Sleep, WaitMode.NoWait],
    [tc.SetBuiltinDetumblingBlockMaskTelecommand(5, 0), Send, WaitMode.NoWait],
    [2, Sleep, WaitMode.NoWait],
    [tc.SetBuiltinDetumblingBlockMaskTelecommand(6, 0), Send, WaitMode.NoWait],
    [2, Sleep, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]