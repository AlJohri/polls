'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:HPCtrl
 * @description
 * # HPCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('HPCtrl', function ($scope) {
  	$scope.status = $scope.$parent.status;
    $scope.hp = $scope.$parent.hp;
    $scope.refreshHP = $scope.$parent.refreshHP;
  });
