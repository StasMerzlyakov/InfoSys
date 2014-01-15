/* 
 * Copyright 2013, Merzliakov Stas
 * Licensed under the MIT licenses.
 */
(function($) {

  // Список плагинов
  pluginMap  = {
    'checkBox' : function(tr) {
      var object = $(this);
      // добавляем свой 
      var chSpan = $('<span/>');

      // проверяем состояние родителя - если он выделен - добавляем выделение к tr
      var parentId = getParentNodeId(tr);
      if (parentId!=null){
        var pclass = '.treegrid-' + parentId;
        var selector = pclass + ' span.checked, ' + pclass + ' span.unchecked';
        // а что если each работает параллельно
        object.find(selector).each(function(){
          var pchSpan = $(this);
          if (pchSpan.hasClass('checked')) {
            chSpan.addClass('glyphicon glyphicon-check checked');
          } 
          if (pchSpan.hasClass('unchecked')){
            chSpan.addClass('glyphicon glyphicon-unchecked unchecked'); 
          }
        });
      } else {
        chSpan.addClass('glyphicon glyphicon-unchecked unchecked');
      }
      chSpan.on('click', onCheckFn);
      var lastSpan = tr.find('span').last();
      if (lastSpan !=undefined && lastSpan !=null){
        lastSpan.after(chSpan);  
      } else {
        tr.append(chSpan);
      }      
      
      return tr;
    }
    
  }

  // Функция снятия флага выбора элемента
  uncheckFn = function(){
    var chSpan = $(this);
    if (chSpan.hasClass('checked')) {
      chSpan.removeClass('glyphicon glyphicon-check checked');
      chSpan.addClass('glyphicon glyphicon-unchecked unchecked');
    }
   
    // Распростроняем выделение на все дочерние объекты
    var tr=chSpan.parents('div.row');
    var nodeId = getNodeId(tr);
    var pclass = '.treegrid-parent-'+ nodeId;
    var selector = pclass + ' span.checked, ' + pclass + ' span.unchecked';
    var object = tr.parent();
    object.find(selector).each(function(){
      uncheckFn.call(this);
    });

  }


  // Функция снятия выделения с родителя
  uncheckParent = function(){
    var tr = $(this);
    // Снимаем флаг с родительского элемента
    var parentNodeId = getParentNodeId(tr);
    var pclass = '.treegrid-' + parentNodeId;
    var object = tr.parent();

    // Селектор для span родителя
    var selector = pclass + ' span.checked';
    // Ищем родителя
    object.find(selector).each(function(){
      var chSpan = $(this);
      var tr=chSpan.parents('div.row');
      chSpan.removeClass('glyphicon glyphicon-check checked');
      chSpan.addClass('glyphicon glyphicon-unchecked unchecked');
      uncheckParent.call(tr);
    });
  }

  // Функция проверки и установки про необходимости флага выбора элемента
  checkParent = function(){
    
    var tr = $(this);

    // Проверяем всех потомков родителя
    var parentNodeId = getParentNodeId(tr);
    var parentclass = '.treegrid-parent-' + parentNodeId;
    var pidclass = '.treegrid-' + parentNodeId;
    var object = tr.parent();

    // Ищем родителя, устанавливаем на него выделение.
    // Потом проверяем всех потомков - если есть не выделенный 
    // снимаем выделение с родителя.
    // Если родитель остался веделеным - проверяем родителя родителя.
    
    var selector = pidclass + ' span.unchecked, ' + pidclass + ' span.checked';
    object.find(selector).each(function(){
      // Нашли span родителя
      var parentSpan = $(this);
      parentSpan.removeClass('glyphicon glyphicon-check checked');
      parentSpan.removeClass('glyphicon glyphicon-unchecked unchecked');
      parentSpan.addClass('glyphicon glyphicon-check checked');
      
      // новый селектор на дочерний не выделеный элемент.
      var selector = parentclass + ' span.unchecked';
      object.find(selector).each(function(){
        // что-то нашли - снимаем выделение с родителя.
        parentSpan.removeClass('glyphicon glyphicon-check checked');
        parentSpan.addClass('glyphicon glyphicon-unchecked unchecked');
        // выходим из цикла
        return false;         
      });
      // Если родитель остался выделеным  проверяем родителя родителя
      if (parentSpan.hasClass('checked')){
        object.find(pidclass).each(function(){
          checkParent.call(this);
        });
      }
    
    }); 
  }

  // Функция установки флага выбора элемента
  checkFn = function(){
    var chSpan = $(this);
    if (chSpan.hasClass('unchecked')) {
      chSpan.removeClass('glyphicon glyphicon-unchecked unchecked');
      chSpan.addClass('glyphicon glyphicon-check checked');
    }
    // Распростроняем выделение на все дочерние объекты
    var tr=chSpan.parents('div.row');
    var nodeId = getNodeId(tr);
    var pclass = '.treegrid-parent-'+ nodeId;
    var object = tr.parent();
    object.find(pclass).each(function(){
      $(this).find('span.unchecked, span.checked').each( function(){
        checkFn.call(this);
      });
    });
    
  }

  // Функция обработки выбора элемента
  onCheckFn = function(){
    var chSpan = $(this);
    var tr=chSpan.parents('div.row');
    if (chSpan.hasClass('unchecked')){
      checkFn.call(this);
      // Проверка и установка, при необходимости, выделения на родителе, 
      checkParent.call(tr);
    } else {
      uncheckFn.call(this);
      // Снимаем выделение с родителя
      uncheckParent.call(tr);
    }
  }

  // Функция получения нужной настройки
  getSettings = function(object, name){
    var settings = $.data(object, 'TreeGrid')['settings'];
    return settings[name]; 
  },


  // 
  // Функция загрузки данных.
  // Пока загружает все.
  //
  loadData = function(object){
    var url = getSettings(object, 'url');
    var levelFieldName = getSettings(object, 'level');
    var data = {};
    data[levelFieldName] = JSON.stringify(['eq', 0]);
    $.ajax({
      url: url,
      dataType: 'jsonp',
      data : data,
      context: object
    }).done(function(data){
      showData(this, data);
    }).fail(function() {
      alert( "ошибка при загрузке " + url );
    });
  },

  getNodeId = function(node) {
    var template = /treegrid-([A-Za-z0-9_-]+)/;
    if (template.test(node.attr('class'))) {
      return template.exec(node.attr('class'))[1];
    }
    return null;
  },

  getParentNodeId = function(node) {
    var template = /treegrid-parent-([A-Za-z0-9_-]+)/;
    if (template.test(node.attr('class'))) {
      return template.exec(node.attr('class'))[1];
    }
    return null;
  },

  // Функция-обработчик события клика мыши для раскрытия компонента
  toggleNode =function(object){
    var pidFieldName = getSettings(object,  "pid");
    var url = getSettings(object, "url");
    var spexp = $(this);
    var tr=spexp.parents('div.row');
    var nodeId = getNodeId(tr);
    var pclass = '.treegrid-parent-'+ nodeId;
    if (spexp.hasClass('treegrid-collapsed')){
      spexp.removeClass('treegrid-collapsed');
      spexp.addClass('treegrid-expanded');
      if (spexp.hasClass('glyphicon glyphicon-chevron-right')){
        spexp.removeClass('glyphicon glyphicon-chevron-right');
        spexp.addClass('glyphicon glyphicon-chevron-down');
      }
      if (spexp.hasClass('child-not-loaded')){
        // Загружаем потомков и добавляем после родителя
        var data = {};
        data[pidFieldName]=JSON.stringify(['eq',nodeId]);
        $.ajax({
          url: url,
          dataType: 'jsonp',
          data : data,
        }).done(function(data){
          var arr = data["items"];     
          arr.forEach(function(item) {
            var childtr = createRecord.call(item, object);
            tr.after(childtr);
            childtr.show();
            spexp.removeClass('child-not-loaded'); 
          });
        }).fail(function() {
          alert( "ошибка при загрузке " + url );
        });
      } else {
        // Просто показываем потомков
        object.find(pclass).each(function(i,val){
          showRecursive.call(val);
        }); 
      }
    }  
    else {
      spexp.removeClass('treegrid-expanded'); 
      spexp.addClass('treegrid-collapsed');
      if (spexp.hasClass('glyphicon glyphicon-chevron-down')){
        spexp.removeClass('glyphicon glyphicon-chevron-down');
        spexp.addClass('glyphicon glyphicon-chevron-right');
      }
      object.find(pclass).each(function(i,val){
        // скрываем элемент
        hideRecursive.call(val);
      });
     }
  },   

  // Раскрытие элементов рекурсивно
  showRecursive = function(){
    var tr = $(this);
    tr.show();
    tr.find('span.treegrid-expanded').each(function(i,span){
      // Если узел был раскрыт - показываем потомков 
      var trId = getNodeId(tr);
      var pclass = '.treegrid-parent-'+ trId;
      var object = tr.parent();
      object.find(pclass).each(function(i,trow){
        showRecursive.call(trow);
      });
   });
  },

  //
  // Скрытие дочерних элементов рекурсивно
  // 
  hideRecursive = function(){
    var tr = $(this);
    tr.hide();
    var trId = getNodeId(tr);
    var pclass = '.treegrid-parent-'+ trId;
    var object = tr.parent();
    object.find(pclass).each(function(i,val){
      hideRecursive.call(val);
    });
  },

  // 
  // Функция создания tr
  //
  createRecord = function(object){
      var oidFieldName = getSettings(object,  "oid");
      var pidFieldName = getSettings(object,  "pid");
      var nameFieldName = getSettings(object, "name");
      var levelFieldName = getSettings(object, "level");
      var hasChildFieldName=getSettings(object, "hasChild");
      var url = getSettings(object, "url");
      var item = this;
      var tr = $("<div/>");
      tr.addClass("row");
      var plugins = getSettings(object, "plugins");

      tr.addClass('treegrid-'+ item[oidFieldName]);

      // если есть родитель
      if (item[pidFieldName] != null){
        tr.addClass('treegrid-parent-'+item[pidFieldName]);
        tr.hide();
      }
      
      var td = $("<div/>");
      td.addClass("col-md-9");

      td.appendTo(tr);
      for (var i =0; i< item[levelFieldName]; i++){
        var spind = $("<span/>");  
        spind.addClass("treegrid-indent");
        spind.appendTo(td);
      }
      var spexp = $("<span/>");  
      spexp.addClass("treegrid-collapsed");
      if (item[hasChildFieldName]) {
        spexp.addClass('glyphicon glyphicon-chevron-right');
        spexp.addClass('child-not-loaded');
        spexp.on('click',function() {
          toggleNode.call(this, object);
        });
      } else {
        spexp.addClass("treegrid-indent");
        spexp.appendTo(td);
      }
      spexp.appendTo(td);
      td.append(item[nameFieldName]);
      plugins.forEach(function(item){
        var pluginFun = pluginMap[item];
        if (pluginFun != undefined ) {
          
          tr = pluginFun.call(object,tr);
        }
      });
      
      return tr;
    }

  


  //
  // Отображение данных дерева.
  // отображаем только узел с level=0, остальные узлы прячем
  // 
  showData=function(object, data){

    var arr = data["items"];     
    arr.forEach(function(item) {
      var tr = createRecord.call(item, object);
      tr.appendTo(object); 
    });

  }

 
  //
  // Инициализация дерева.
  // Для каждого дерева в $.data добавляется структура с настройками
  // @param {Object[]} selector
  // @param {Object} options
  // @returns {Object[]}
  //
  initTree = function(selector,options) {
    selector.each(function(i,val){
      var $val=$(val);
      setSettings($val, options);
      loadData($val);
    }); 
   return selector;
  };

  // 
  // Функция привязки настроек к объекту дерева
  // @param {Object} object
  // @param {Array} options
  // @return {Object} 
  // 
  setSettings = function(object,options){
    var settings = $.extend({}, $.fn.TreeGrid.defaults, options );
    var data = {};
    data['settings'] = settings;
    $.data(object, 'TreeGrid', data);
    return object;
  }

  //
  // Основная функция инициализации
  // Параметры:
  // ---------------------------------------
  //   имя  : значение по-умолчанию // комментарий
  // ---------------------------------------
  //   url  :  undefined            // адрес хранилища
  //   oid  : 'id'                  // имя первичного ключа
  //   pid  : 'pid'                 // имя поля - внешнего ключа на родителя
  //   level: 'level'               // поле, определяющее уровень вложенности объекта
  //   name : 'name'                // имя поля с содержимым записи
  //   hasChild : 'isParent'        // поле, указывающее есть ли потомки у узла
  //   plugins  : []                // список плагинов
  // 
  //
  $.fn.TreeGrid = function(options) {
    return initTree(this, options);
  }

  // 
  // Настройки по-умолчанию
  // 
  $.fn.TreeGrid.defaults = {
     oid : 'id',
     pid : 'pid',
     name : 'name', 
     level: 'level',
     hasChild: 'isParent',
     plugins : []
  }
 
  //
  // Прототип моделей
  // 
  TreeGridModel = {};   
  
  TreeGridModel.prototype = { 
    getItems : function() {
          
    }
  }; 
})(jQuery);


