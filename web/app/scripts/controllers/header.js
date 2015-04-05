'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('HeaderCtrl', function ($scope, Ref, $location) {
  	$scope.isActive = function (viewLocation) {
  		// console.log(viewLocation + " " + $location.path());
  		// var truthy = viewLocation === $location.path();
  		// console.log(truthy);
        return viewLocation === $location.path();
    };
});