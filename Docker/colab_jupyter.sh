source /opt/ros/noetic/setup.bash
export ROS_IP=127.0.0.1

jupyter notebook \
    --NotebookApp.allow_origin='https://colab.research.google.com' \
    --NotebookApp.token='assistive' \
    --NotebookApp.port_retries=0 \
    --notebook-dir /home/arg/arg_tools \
    --port=8888 \
    --allow-root \
    --no-browser \
    --ip=0.0.0.0
#    --ip=localhost

