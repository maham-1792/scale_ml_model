# scale_ml_model
1. Install Minikube and deploy any ML model on a pod and show the use of pods through NodePort or LoadBalancer through Minikube IP. You must show the running pod, its IP, and any services you run to enable the POD to communicate outside the Kubernetes cluster. You also need to show the curl command or web UI to show the use of the service. 

2. Deploy the pod you used in the previous step through the deployment object using a different number of replicas like 1, 2, 3, 4, and 5. The output of the ML model should show the IP address of the POD/Container serving the request. 

3. Deploy your ML model with 1 POD and run a workload generator in a step-up fashion to identify the CPU saturation. You can use any application in the POD to ensure its CPU saturates when the number of requests is increased. Once you identify the X number of requests that are saturating the CPU then you need to manually update you deployment to two PODs and then show the performance on X number of requests using 2 POD. 


4.  Autoscaling in Kubernetes for your POD. Do some R&D and find out how to do autoscaling in Kubernetes for your POD. 
