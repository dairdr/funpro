var Main = (function (window, undefined) {
    var _dom = {
        testForm: '#test'
    };
    var _events = {
        click: 'click',
        submit: 'submit'
    };
    var _actRef = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41];
    var _senInt = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42];
    var _visVrb = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43];
    var _secGlo = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44];
    var _rule = [11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11];

    /**
     * 
     * @returns {undefined}
     */
    function init() {
        config();
        addEventListeners();
    }
    
    /**
     * 
     * @returns {undefined}
     */
    function config(){}

    /**
     * 
     * @returns {undefined}
     */
    function addEventListeners() {
        $(_dom.testForm).on(_events.submit, onSubmitFormCallback);
    }

    /**
     * 
     * @param {type} event
     * @returns {undefined}
     */
    function onSubmitFormCallback(event) {
        if (event.preventDefault) {
            event.preventDefault();
            var total = $(_dom.testForm + ' div.item').length;
            var totalSelected = $(_dom.testForm + ' input:checked').length;
            if (totalSelected === total) {
                event.target.submit();
                /*var g1 = checkAnswers(_actRef);
                 var g2 = checkAnswers(_senInt);
                 var g3 = checkAnswers(_visVrb);
                 var g4 = checkAnswers(_secGlo);
                 console.log('g1=%s, g2=%s, g3=%s, g4=%s',g1,g2,g3,g4);*/
            } else {
                new Messi('Por favor, complete el formulario.', {
                    title: 'Mensaje',
                    modal: true,
                    titleClass: 'error',
                    buttons: [{id: 0, label: 'Aceptar', val: 'c'}]
                });
            }
        }
    }

    /**
     * 
     * @param {type} array
     * @returns {Number}
     */
    function checkAnswers(array) {
        var countA = 0;
        var countB = 0;
        for (var item in array) {
            var option = $(_dom.testForm + ' div.item-' + String(array[item])).find('input:checked').val();
            (option === 'a') ? countA += 1 : countB += 1;
        }
        return countA - countB;
    }

    return {
        init: init
    };
}(window));

Main.init();