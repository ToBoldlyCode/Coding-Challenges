def solveCaptcha2(captcha):
  solution = 0
  step = len(captcha)//2
  for i in range(0, len(captcha)):
    if captcha[i] == captcha[(i+step) % len(captcha)]:
      solution += int(captcha[i])
  print(solution)