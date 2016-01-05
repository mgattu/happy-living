(function () {  
    function CustomerController($scope,$log, CustomerService) {


        $scope.users = [];

    
        function init(){
           
            CustomerService.userList()
            
            .success(function(users){
                $scope.users = users;
            })
            
            .error(function(data,status,headers,config){
                // Error Handling
                //$log.log('data:'+data+'status'+status+'headers'+headers+'config'+config);
                //alert("Error"+data+status);
            });
        }
        
        init();

        

        $scope.register = function () {
            CustomerService.register($scope.vm);
        }; 

        $scope.login = function () {
            CustomerService.register($scope.email, $scope.password);
        }; 

        $scope.list = function () {
            CustomerService.userList();
        }; 

        $scope.editCustomerdetails = function () {
            CustomerService.register($scope.email, $scope.password, $scope.first_name);
        }; 
    };
    
    angular.module('happyApp').controller('CustomerController',CustomerController);
           
}());