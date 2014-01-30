###
    Инициализация списка компаний InfoSys
###
(
  ($) ->
    $.fn.extend
      loadOList : (options) ->
        settings =
          debug : false

        settings = $.fn.extend settings, options

        log = (msg) ->
          console?.log(msg) if settings.debug

        initTree = (selector, options) ->
          log 'load from url:' + options.url
          selector.each (i,val)->
            # Загрузка данных
            $.ajax options.url,
              dataType: 'jsonp'
              error: ()->
                alert 'Ошибка при  загрузке' + url
              success: (data) ->
                log data  
          selector

        initTree this, options
        log 'InfoSys OK'
) jQuery





