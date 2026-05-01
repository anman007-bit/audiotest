[app]
title = Тест звука
package.name = audiotest
package.domain = org.myfamily
source.dir = .
source.include_patterns = sounds/*
source.include_exts = py,png,jpg,kv,atlas,ttf,mp3,wav,ogg
version = 1.0
requirements = python3,kivy==2.3.0
orientation = landscape
fullscreen = 0
android.permissions = 
android.minapi = 21
android.api = 33
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
