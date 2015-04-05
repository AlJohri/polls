'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('MainCtrl', function ($scope) {

    $scope.status = $scope.$parent.status;
    $scope.refreshAll = $scope.$parent.refreshAll;

  });
