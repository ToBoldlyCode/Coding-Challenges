def solveCaptcha(captcha):
    solution = 0
    for i in range(0, len(captcha)):
      if captcha[i] == captcha[(i+1) % len(captcha)]:
        solution += int(captcha[i])
    print(solution)