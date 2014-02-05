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
          
        # Создание блока с представлением организации
        # Формируется блок вида
        #  <div class="row">
        #    <div class="col-md-6 col-md-offset-3">
        #      <h3><a href="#">ЗАО Пиво и воды</a></h3>
        #      <h4>(Удмуртия, Ижевск)</h4>
        #      <h5>Ключевые слова</h5>
        #      <h6>Общее описание</h6>
        #      <a class="btn btn-info pull-right btn-xs">В список</a>   
        #    </div>
        #  </div
        #
        createRow = (row) ->
          rowEl = $ '<div>'
          rowEl.addClass 'row'
          colEl = $ '<div>'
          colEl.addClass 'col-md-6 col-md-offset-3'
          rowEl.append colEl
          
          # <h3><a href="#">row.name</a></h3>
          nameEl = $ '<h3>'
          colEl.append nameEl
          aEl = $ '<a>'
          aEl.attr 'href', '#'
          nameEl.append aEl
          aEl.text row.name
          
          # <h4>(row.placeinfo)</h4>
          placeEl = $ '<h4>'
          colEl.append placeEl
          placeEl.text '(' + row.placeinfo + ')'

          # <h5>row.keywords</h5>
          keywordsEl = $ '<h5>'
          keywordsEl.addClass 'bold'
          colEl.append keywordsEl
          keywordsEl.text row.keywords

          
          # <h6>row.shortinfo</h6>
          infoEl = $ '<h6>'
          colEl.append infoEl
          infoEl.text row.shortinfo
          
          # <a class="btn btn-info pull-right btn-xs">В список</a>
          aEl = $ '<a>'
          colEl.append aEl
          aEl.addClass 'btn btn-info pull-right btn-xs'
          aEl.text 'В список'
          
          
          # Возвращаем элемент
          rowEl
          
          
          
        
        # Инициализация списка организаций
        initTree = (selector, options) ->
          log 'load from url:' + options.url
          selector.each (i,val)->
            # Загрузка данных
            $.ajax options.url,
              dataType: 'jsonp'
              error: ()->
                alert 'Ошибка при  загрузке' + options.url
              success: (data) ->
                log data
                data.items.forEach (item) ->
                  row = createRow item
                  container = $ val 
                  container.append row
                 
          selector

        initTree this, options
        
        log 'InfoSys OK'
) jQuery





