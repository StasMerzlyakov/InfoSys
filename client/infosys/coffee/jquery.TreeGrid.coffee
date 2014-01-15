###
 Для произвольного использования.
###
(
  ($) ->


    $.fn.extend
      TreeGrid : (options) ->
        
        ### Настройки по-умолчанию ###
        settings =
          debug : false   ## Флаг отладки
          oid : 'id'      ## название поля ПК
          name : 'name'   ## название поля 'Имя'
          level : 'level' ## название поля 'Уровень вложенности'
          hasChild : 'isParent' ## название поля 'Флаг родителя'
          
    
        settings = $.fn.extend settings, options
        
        ## Функция логирования
        log = (msg) ->
          console?.log(msg) if settings.debug

        $.each settings, (ind, val)->
          log ind + ":" + val

        ## Фунция привязки настроек к объекту
        setSettings  = (object, settings)->
          data = { 'settings' : settings }
          $.data object, 'TreeGrid', data
          object

        selector = this
        selector.each (i, val) ->
          $val = $(val)
          log $val
          setSettings $val, settings
        selector


) jQuery



