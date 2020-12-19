## Description
This adds a plugin for precise, this is the official mycroft wake word 
engine and is supported out of the box by core, however i have some issues 
with the official implementation that i try to solve with this

- the downloading of binaries is messy, i prefer that the download blocks 
  instead of reloading the listener
- mycroft-core keeps replacing and redownloading binary whenever you test a 
  new model from a different version, i want to support having both versions 
  side by side
  - i support [multiple wakeword at same time](https://github.com/MycroftAI/mycroft-core/pull/1233)
- xdg compliant paths
- allow overriding binary used
- fix recording of wake words setting, this is derived from phonemes and 
  badly implemented in core, so you end up getting 0.2 second recordings etc

The "plugins" are pip install-able modules that provide new engines for mycroft

more info in the [docs](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins)

## Install

`mycroft-pip install chatterbox-wake-word-plugin-precise`

Configure your wake word in mycroft.conf

```json
 "listener": {
      "wake_word": "android"
 },
 "hotwords": {
    "android": {
        "module": "jarbas_precise_ww_plug",
        "version": 0.3,
        "model": "path/to/your/model"
    }
  }
 
```

Advanced configuration

```json
 "listener": {
      "wake_word": "android"
 },
 "hotwords": {
    "android": {
        "module": "jarbas_precise_ww_plug",
        "trigger_level": 3,
        "sensitivity": 0.5,
        "version": 0.3,
        "model": "path/to/your/model",
        "binary_path": "path/to/your/binary/eg/using/tflite",
        "expected_duration": 3
    }
  }
 
```


- `binary_path` if you want to use your own binary, eg for use with 
  [tflite branch](https://github.com/MycroftAI/mycroft-precise/pull/141)
- `version` defaults to 0.2, only 0.2 and 0.3 supported (ignored if binary path is set)
- `model` full path to your model file, if version is 0.2 and wakeword 
name is "hey mycroft" the default model will be used and this is optional
- `trigger_level` Higher = more delay & less sensitive
- `sensitivity`  Higher = more sensitive
- `expected_duration` defaults to 3 seconds (max value), this is the time 
  used for [saving wake word samples](https://github.com/MycroftAI/mycroft-core/blob/4c84f66e15a361d9f3d650def1ba97fa80506456/mycroft/configuration/mycroft.conf#L160)