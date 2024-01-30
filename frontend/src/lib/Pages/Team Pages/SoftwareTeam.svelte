<script lang="ts">
  import AliElGuindy from '../../../assets/OC/SoftwareTeam/Ali Guindy.jpg';
  import NavBar from "../../Components/NavBar.svelte";
  import KhaledDawoud from '../../../assets/OC/SoftwareTeam/Khaled Dawoud2.jpg';
  import HeadShot from "../../Components/HeadShot.svelte";
  import MuhammedElKhedr from '../../../assets/OC/SoftwareTeam/Muhammed elkhedr.jpg';
  import GroupSection from '../../Components/GroupSection.svelte';


</script>

<body class="bg-cover bg-no-repeat bg-center" >
    <NavBar />

    <div class="p-10">
        <h1 class="text-center text-4xl font-bold mb-2"> Our Software Developers </h1>
        <hr class="mb-10">
        <div class="mb-6">
            <GroupSection link={null} noReadMe={true} header="Khaled Dawoud - Head of Software" text={null} image={KhaledDawoud} />
        </div>
            <div class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
                <HeadShot name="Ali El Guindy" title="UI Designer" image={AliElGuindy} quote="Hi all, I'm Ali. I was the UI designer for ALSMUN's website.I hope you like it."/>
                <HeadShot name="Muhammed El Khedr" title="Frontend Developer" image={MuhammedElKhedr} quote="Hey everybody, my name is Muhammad Elkhedr and I was a front-end developer for ALSMUN's website. We spent many enjoyable months working on this, and I hope you enjoy it too."/>
            </div>
    </div>
</body>