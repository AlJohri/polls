'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:HPCtrl
 * @description
 * # HPCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('HPCtrl', function ($scope, Ref, $firebaseArray, $timeout, $http, $q) {

    $scope.hp = $firebaseArray(Ref.child('hp'));
    $scope.hp.$loaded().catch(alert);

    function alert(msg) {
      $scope.err = msg;
      $timeout(function() {
        $scope.err = null;
      }, 5000);
    }

    $scope.refreshHP = function() {
      $http.get("http://todayspolls.herokuapp.com/hp")
    }

  });
