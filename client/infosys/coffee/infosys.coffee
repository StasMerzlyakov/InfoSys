###
    Инициализация списка компаний InfoSys
###
(
  ($) ->
    $.fn.extend
      InfoSys : (options) ->
        settings =
          debug : false
      
        settings = $.fn.extend settings, options

        log = (msg) ->
          console?.log(msg) if settings.debug

        log 'InfoSys OK'
) jQuery





