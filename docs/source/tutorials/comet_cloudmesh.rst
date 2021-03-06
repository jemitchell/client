Comet Cloudmesh Tutorial
=========================

Setup Cloudmesh Client on Ubuntu Desktop in Virtualbox

.. note:: Scripts used in this tutorial are maintained at:

   * https://github.com/sdsc/comet-vc-tutorial

Virtual Box
----------------------------------------------------------------------

**Step 1:** For convenience we will be using Ubuntu Xenial in this
demo to install the Cloudmesh client on it. Please make sure you have

* `VirtualBox <https://www.virtualbox.org>`_ installed (`downloads page <https://www.virtualbox.org/wiki/Downloads>`_).

**Step 2:** Next, please download the

* `Ubuntu desktop ISO <http://www.ubuntu.com/download>`_.

and remember the location where you downloaded it. You will need that
location later.

**Step 3:** Create VirtualBox, create a new VM (Ubuntu, 64bit)

**Step 4:** Start the box. When asked for the ISO, use the folder icon
 to browse to the location of the downloaded image.

**Step 5:** Start and configure the system. Note in case the last step
 does not return, shut down or terminate the VM and restart it.

**Step 6:** Once you have logged into the vm, start a terminal by
 clicking on the cog and type in *terminal*

**Step 7:** (optional) You may want to enable the vm guest addition
and enable bidirectional shared clipboard and drag and drop. You may
have to restart the vm so that these changes take effect.

**Step 8:** Install cloudmesh. Paste and copy between host and vm, as
 well as .

.. note: as well as . is unclear .... FIX
  
.. prompt:: bash, cloudmesh$

    wget -O cm-setup.sh http://bit.ly/cloudmesh-client-xenial
    sh cm-setup.sh

The script has the following contents::

    sudo apt install python-pip -y
    sudo apt install libssl-dev -y
    sudo pip install pip -U
    sudo apt install git -y
    sudo pip install ansible
    sudo pip install cloudmesh_client
    python --version
    pip --version
    git –version



Configure Cloudmesh
-------------------

Next, we need to configure Cloudmesh. We will only use a fraction of
Cloudmesh capabilities for this tutorial that is focused on using
comet

.. prompt:: bash, cloudmesh$

   ssh-keygen
   cm
   cm version

    
Instalation with Pip
----------------------------------------------------------------------

Installing in a virtualenv is highly recommended.

.. prompt:: bash, cloudmesh$

  pip install cloudmesh_client
  cm help
  cm comet init

Virtual Cluster Architecture
----------------------------------------------------------------------

.. figure:: ./images/vc-diagram.png
   :scale: 50 %
   :alt: screenshot

   Figure: Virtual cluster architecture
 
Getting access to your cluster
----------------------------------------------------------------------

Access your virtual cluster (vc)

The cluster information can be obtained with the following commands:

.. prompt:: bash, cloudmesh$

  cm comet ll 
  cm comet cluster
  cm comet cluster vct<NN>

The list of ISO images that are currently available can be obtained with:

.. prompt:: bash, cloudmesh$

  cm comet iso list

.. note: in future versions the command iso may be renamed to *image*.

Example: Install the front-end node
----------------------------------------------------------------------

Find an iso and attach

.. prompt:: bash, cloudmesh$

  cm comet iso list

This will return::

   1: CentOS-7-x86_64-NetInstall-1511.iso
   2: CentOS-6.8-x86_64-netinstall.iso
   3: kernel-6.2-0.x86_64.disk1.iso
   4: systemrescuecd-x86-4.2.0.iso
   5: base+kernel+kvm+os-6.2.x86_64.disk1.iso
   6: ubuntu-14.04.4-server-amd64.iso
   7: ubuntu-15.04-server-amd64.iso
   8: CentOS-6.8-x86_64-LiveDVD.iso
   9: ubuntu-16.04-server-amd64.iso
  10: CentOS-7-x86_64-LiveGNOME-1511.iso

Next we attach an iso. YOu can use either the name of the iso, or simply the id

.. prompt:: bash, cloudmesh$

  cm comet iso attach 6 vct<NN>


Let us check the status of the server.

.. prompt:: bash, cloudmesh$

   cm comet cluster vct<NN>

If it is already running, please power if off so the iso attach could
take effect:

.. prompt:: bash, cloudmesh$

  cm comet power off vct<NN>

Now we need to power on the server

.. prompt:: bash, cloudmesh$

  cm comet power on vct<NN>

To see what is happening on the server, we can attach a console to follow and complete the setup of the OS

.. prompt:: bash, cloudmesh$

  cm comet console vct<NN>

Screenshots for the front-end node configuration are given next:

.. figure:: ./images/00_install_start.png
   :scale: 50 %
   :alt: screenshot

   Figure: Install ubuntu server

.. figure:: ./images/01_NIC.png
   :scale: 50 %
   :alt: screenshot

   Figure: Configure the network. DHCP is configured on `eth1` (the public interface)

.. figure:: ./images/20_hostname.png
   :scale: 50 %
   :alt: screenshot

   Figure: Set the hostname

.. figure:: ./images/22_user_password_creation.png
   :scale: 50 %
   :alt: screenshot

   Figure: Set up the non-privileged user account, including a strong password

.. figure:: ./images/08_partition.png
   :scale: 50 %
   :alt: screenshot

   Figure: Partition the disk

.. figure:: ./images/09_services_packages.png
   :scale: 50 %
   :alt: screenshot

   Figure: Select OpenSSH using the space bar and then tab to Continue

.. figure:: ./images/10_complete.png
   :scale: 50 %
   :alt: screenshot

   Figure: Complete the installation

.. figure:: ./images/11_complete_console_expired.png
   :scale: 50 %
   :alt: screenshot

   Figure: Press CONTINUE (we'll detach the ISO later)

.. figure:: ./images/12_reboot_cd.png
   :scale: 50 %
   :alt: screenshot

   Figure: The machine will be rebooted. Allow it to start booting from the CDROM again.

.. figure:: ./images/13_reboot_cd_choose_hd.png
   :scale: 50 %
   :alt: screenshot

   Figure: From the CDROM boot menu, choose to boot from hard disk


Finishing Front-end setup
----------------------------------------------------------------------

At end of the installation, click **complete** to finish the setup. The node will
reboot into the OS installation CD again, but now choose 'boot from first hard disk'
option from the booting menu. This ensure the node boots into the newly installed OS,
while having the OS installation CD still attached (we will need the CD again in the
later steps).

Once the node is back on, you can now login and configure the cluster from your laptop/desktop:

.. prompt:: bash, cloudmesh$

  cm comet console vct<NN>

YOu can also ssh into the machine after it is configures with the usual ssh commands while
using your login name that you set up and specify your cluster name.

.. prompt:: bash, cloudmesh$

  ssh USER@vct<NN>.sdsc.edu

Configuring the front-end node
----------------------------------------------------------------------

On your managing machine where Cloudmesh client tools is installed:

If your **managing** machine is running Linux:

.. prompt:: bash, cloudmesh$

  wget -O cmutil.py http://bit.ly/vc-cmutil
  python cmutil.py nodesfile vct<NN>
  scp vcn*.txt <USER>@vct<NN>.sdsc.edu:~/

If your **managing** machine is running Mac OS X use curl instead of wget:

.. prompt:: bash, cloudmesh$

     curl -L -o cmutil.py http://bit.ly/vc-cmutil
     python cmutil.py nodesfile vct<NN>
     scp vcn*.txt <USER>@vct<NN>.sdsc.edu:~/

On the vc **front-end** node:

.. prompt:: bash, fe$

  wget -O deploy.sh http://bit.ly/vc-deployment
  chmod +x deploy.sh
  sudo ./deploy.sh

At this point we are done with the ISO and back on your **managing**
machine you should detach it:

.. prompt:: bash, cloudmesh$

  cm comet iso detach vct<NN>

ISO are removed the next time the virtual node is shutdown or powered
off (not when  rebooted or reset).

  
Example: Install Compute Nodes
----------------------------------------------------------------------

Compute node setup

.. prompt:: bash, cloudmesh$

   cm comet start vct<NN> vm-vct<NN>-[1-2]

Takes about 15~20 minutes. Once done, the node will be shutoff.

Once you see the boot question in your console log, please change it to
localboot. Do this on the front-end node:

.. prompt:: bash, fe$

  cd $HOME
  sudo ./comet-vc-tutorial/cmutil.py setboot $HOSTNAME vm-vct01-01 net=false

You will also need to generate an SSH keypair for your non-privileged
user account and create an ``authorized_keys`` file to allow your
parallel application to access both nodes. This key pair is only for
use within the cluster since it will not have a passphrase. Just hit
enter at each step.

.. prompt:: bash, fe$

  cd $HOME
  ssh-keygen
  cat .ssh/id_rsa.pub >> .ssh/authorized_keys
  
Then on your managing host where Cloudmesh client is installed:

.. prompt:: bash, cloudmesh$

  cm comet power on vct<NN> vm-vct<NN>-[1-2]

Wait for the compute nodes to be booted on, which can be checked by:

.. prompt:: bash, cloudmesh$

  cm comet cluster vct<NN>

to see if the state (2nd column) of the nodes is 'active'.

Once the compute nodes are on, run these on the front-end node:

.. prompt:: bash, fe$

  sudo $HOME/comet-vc-tutorial/key_setup.sh

This will propagate the non-privileged user's password to the compute
nodes securely.

Login to compute nodes from front-end, and run your app.

.. note:: In the production environment we use two factor
          authentication with `YubiKeys <https://www.yubico.com/>`_ to
          retrieve the API token used to by Cloudmesh and to access
          the console of a virtual machine. To simplify the tutorial
          we use username and password access in an isolated teaching
          environment. When utilizing the production version you will
          need to get in contact with the Comet staff. You must have a
          valid XSEDE allocation on Comet for a virtual cluster.

Verifying InfiniBand Performance
----------------------------------------------------------------------

We'll start by verifying the InfiniBand connectivity between the
compute nodes using RDMA performance tests and the `OSU
Micro-Benchmarks
<http://mvapich.cse.ohio-state.edu/benchmarks/>`_. The InfiniBand tests
are in the Ubuntu ``perftest`` package which is already installed on the
compute nodes. The InfiniBand tests must run as ``root`` so we'll
change to ``root`` on the front-end and then use the SSH keys that are
in place to access the compute nodes.

From your managing machine open two SSH terminals to your virtual
front-end. In one terminal, start a server on the first compute node:

.. prompt:: bash, cloudmesh$

  sudo su -
  ssh vm-vct01-00

Then in that vm type

.. prompt:: bash, vm-vct01-00$

  ib_write_bw 

In the other terminal, connect to the server from the second compute
node and start the test:

.. prompt:: bash, cloudmesh$

  sudo su -
  ssh vm-vct01-01

.. prompt:: bash, vm-vct01-01$
	    
  ib_write_bw vm-vct01-00

The bandwidth results will confirm that we're sending data over InfiniBand::
 
  ------------------------------------------------------------------
                    RDMA_Write BW Test
  Number of qp's running 1
  Connection type : RC
  Each Qp will post up to 100 messages each time
  Inline data is used up to 400 bytes message
    local address:  LID 0x35, QPN 0x09fc, PSN 0x60a317 RKey 0xe00140fc VAddr 0x007f089b60d000
    remote address: LID 0x45, QPN 0x09fc, PSN 0xb1e176, RKey 0x200140fd VAddr 0x007fd1ff5a1000
  Mtu : 2048
  ------------------------------------------------------------------
   #bytes #iterations    BW peak[MB/sec]    BW average[MB/sec]  
    65536        5000            6021.90               6020.33
  ------------------------------------------------------------------

And the first server will show its results in the first terminal::

  ------------------------------------------------------------------
                    RDMA_Write BW Test
  Number of qp's running 1
  Connection type : RC
  Each Qp will post up to 100 messages each time
  Inline data is used up to 400 bytes message
    local address:  LID 0x45, QPN 0x09fc, PSN 0xb1e176 RKey 0x200140fd VAddr 0x007fd1ff5a1000
    remote address: LID 0x35, QPN 0x09fc, PSN 0x60a317, RKey 0xe00140fc VAddr 0x007f089b60d000
  Mtu : 2048
  ------------------------------------------------------------------
   #bytes #iterations    BW peak[MB/sec]    BW average[MB/sec]  

OSU Micro-Benchmarks
----------------------------------------------------------------------

The `OSU Micro-Benchmarks
<http://mvapich.cse.ohio-state.edu/benchmarks/>`_ are suite of
individual applications measuring the latency and bandwidth of
individual MPI calls. The cover both the performance of both the
underlying network fabric and the MPI implementation. The
Micro-Benchmarks provide coverage for the latest MPI standards but the
version of `Open MPI <https://www.open-mpi.org/>`_ in the Ubuntu
Trusty distribution is a bit older and not all of the messaging calls
are available. We'll focus only a few as part of the InfiniBand and
MPI verification.

Begin by logging on to the first compute node where we'll download and
compile the benchmarks. This can be done with your non-privileged user
account. Then download the benchmarks, extract, and configure the
source.

.. prompt:: bash, cloudmesh$
  
  ssh vm-vct01-00

.. prompt:: bash, vm-vct01-00$
  
  wget http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-5.3.tar.gz
  tar -zxf osu-micro-benchmarks-5.3.tar.gz
  cd osu-micro-benchmarks-5.3/
  ./configure CC=/usr/bin/mpicc CXX=/usr/bin/mpicxx

After the source configuration step completes, go into the directory
for the point-to-point communication benchmarks and compile them.

.. prompt:: bash, vm-vct01-00$

  cd mpi/pt2pt/
  make

To run the tests create a host file with the two compute nodes
specified::

  vm-vct01-00
  vm-vct01-01

Remember where you've placed this (``$HOME/two-hosts.txt`` is a good
idea) and run the bandwidth test.

.. prompt:: bash, vm-vct01-00$

   mpirun -np 2 -hostfile ~/two-hosts.txt ./osu_bw

The results will go to the terminal and you can compare them to the
``ib_write_bw`` performance. You can ignore Open MPI's complaints
regarding registered memory, this is due to change in the driver::

  # OSU MPI Bandwidth Test v5.3
  # Size      Bandwidth (MB/s)
  1                       1.56
  2                       3.13
  4                       6.22
  8                      12.63
  16                     24.94
  32                     50.52
  64                     99.95
  128                   188.23
  256                   360.56
  512                   692.32
  1024                 1258.43
  2048                 2178.72
  4096                 3395.65
  8192                 4576.91
  16384                4659.19
  32768                5445.82
  65536                5993.62
  131072               6136.74
  262144               6210.81
  524288               6245.60
  1048576              6242.02
  2097152              6241.21
  4194304              6254.35

Now we'll try a collective benchmark for ``MPI_Alltoall``. We can
reuse our host file for 24 tasks and let MPI distribute the tasks.

.. prompt:: bash, vm-vct01-00$

  cd ../collective/
  make osu_alltoall
  mpirun -np 24 -hostfile ~/two-hosts.txt ./osu_alltoall

Again, there perfomance results (this time for latency) go to the terminal::

   # OSU MPI All-to-All Personalized Exchange Latency Test v5.3
   # Size       Avg Latency(us)
   1                      30.80
   2                      30.54
   4                      30.68
   8                      30.88
   16                     34.35
   32                     35.43
   64                     37.50
   128                    39.63
   256                   136.95
   512                   144.51
   1024                  160.50
   2048                  209.13
   4096                  331.33
   8192                  459.79
   16384                1270.14
   32768                1768.40
   65536                3064.40
   131072               5344.35
   262144              11198.39
   524288              23086.68
   1048576             48169.37

OpenFOAM
----------------------------------------------------------------------

`OpenFOAM <http://openfoam.org/>`_ is a parallel open-source
`computational fluid dynamics
<https://en.wikipedia.org/wiki/Computational_fluid_dynamics>`_
application that is available in a public Ubuntu repository. To
install it, on each of the compute nodes run:

.. prompt:: bash, vm-vct01-00$

   sudo apt install software-properties-common -y
   sudo add-apt-repository http://download.openfoam.org/ubuntu
   sudo apt-get update
   sudo apt-get install openfoam4 -y --force-yes

Add the OpenFOAM profile to your ``.bashrc``:

.. prompt:: bash, vm-vct01-00$

   echo '. /opt/openfoam4/etc/bashrc' >> ~/.bashrc
   source ~/.bashrc
   
We're now able to setup the files and directories needed for a
benchmarking run.

.. prompt:: bash, vm-vct01-00$

   mkdir -p $FOAM_RUN
   cd $FOAM_RUN
   cp -r $FOAM_TUTORIALS/multiphase/interFoam/laminar/damBreak/damBreak .
   foamCloneCase damBreak damBreakFine
   cd damBreakFine
   cp ~/comet-vc-tutorial/examples/OpenFOAM/blockMeshDict system/
   cp ~/comet-vc-tutorial/examples/OpenFOAM/decomposeParDict system/

Setup the mesh and initial conditions.

.. prompt:: bash, vm-vct01-00$

   blockMesh
   cp -r 0/alpha.water.orig 0/alpha.water
   setFields

Decompose the mesh.

.. prompt:: bash, vm-vct01-00$

  decomposePar

Create a host file (``hosts.txt``) and run the code. For example,
create ``hosts.txt`` for 24 tasks on each compute node and run.

.. prompt:: bash, vm-vct01-00$

  echo "vm-vct16-00 slots=24" > hosts.txt
  echo "vm-vct16-01 slots=24" >> hosts.txt
  mpirun  -hostfile ./hosts.txt -np 48 `which foamExec` interFoam -parallel

This will take a while (about 5-10 minutes).
  
The OpenFOAM packages include a version of `ParaView
<http://www.paraview.org/>`_ for OpenFOAM that you can use to view the
mesh. From a system with X windows SSH to your front-end and compute
node with X forwarding enabled.

.. prompt:: bash, vm-vct01-00$

   ssh -X <username>@vct16.sdsc.edu 
   ssh -X vm-vct16-00 
   cd $FOAM_RUN/damBreakFine
   paraFoam -case processor1

.. figure:: ./images/paraview-vct.png
   :scale: 50 %
   :alt: screenshot

   Figure: ParaView with OpenFOAM example data


Julia
----------------------------------------------------------------------

Like OpenFOAM, `Julia <http://julialang.org/>`_ has Ubuntu packages in
public repositories. You can install on the compute nodes following a
similar process. On each compute node run the following commands from
`the Julia installation instructions for Ubuntu
<http://julialang.org/downloads/platform.html>`_. When prompted, hit ``ENTER``.

.. prompt:: bash, vm-vct01-00$

   sudo add-apt-repository ppa:staticfloat/juliareleases
   sudo add-apt-repository ppa:staticfloat/julia-deps
   sudo apt-get update
   sudo apt-get install julia -y


You can start Julia on the command line for interactive use::

   rpwagner@vm-vct01-00:~$ julia
                  _
      _       _ _(_)_     |  A fresh approach to technical computing
     (_)     | (_) (_)    |  Documentation: http://docs.julialang.org
      _ _   _| |_  __ _   |  Type "?help" for help.
     | | | | | | |/ _` |  |
     | | |_| | | | (_| |  |  Version 0.4.6 (2016-06-19 17:16 UTC)
    _/ |\__'_|_|_|\__'_|  |  Official http://julialang.org release
   |__/                   |  x86_64-linux-gnu
   
   julia>


::

    rpwagner@vm-vct01-00:~$ julia --machinefile machinefile-jl.txt 
		   _
       _       _ _(_)_     |  A fresh approach to technical computing
      (_)     | (_) (_)    |  Documentation: http://docs.julialang.org
       _ _   _| |_  __ _   |  Type "?help" for help.
      | | | | | | |/ _` |  |
      | | |_| | | | (_| |  |  Version 0.4.6 (2016-06-19 17:16 UTC)
     _/ |\__'_|_|_|\__'_|  |  Official http://julialang.org release
    |__/                   |  x86_64-linux-gnu

    julia> 
