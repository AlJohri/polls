'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('ContainerCtrl', function ($scope, Ref, $firebaseArray, $timeout, $http, $q) {

    $scope.status = $firebaseArray(Ref.child('status'));
    $scope.status.$loaded().catch(alert);

    $scope.quinnipiac = $firebaseArray(Ref.child('quinnipiac'));
    $scope.quinnipiac.$loaded().catch(alert);

    $scope.hp = $firebaseArray(Ref.child('hp'));
    $scope.hp.$loaded().catch(alert);

    $scope.rcp = $firebaseArray(Ref.child('rcp'));
    $scope.rcp.$loaded().catch(alert);

    $scope.refreshRCP = function() {
      console.log('hello rcp');
      $http.get("http://todayspolls.herokuapp.com/rcp")
    }

    $scope.refreshHP = function() {
      console.log('hello hp');
      $http.get("http://todayspolls.herokuapp.com/hp")
    }

    $scope.refreshQuinnipiac = function() {
      console.log('hello quinnipiac');
      $http.get("http://todayspolls.herokuapp.com/quinnipiac")
    }

    $scope.refreshAll = function() {
      console.log('hello');
      $scope.refreshRCP();
      $scope.refreshHP();
      $scope.refreshQuinnipiac();
    }

});