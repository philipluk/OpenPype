---
id: artist_hosts_houdini
title: Houdini
sidebar_label: Houdini
---

## OpenPype global tools

- [Work Files](artist_tools.md#workfiles)
- [Create](artist_tools.md#creator)
- [Load](artist_tools.md#loader)
- [Manage (Inventory)](artist_tools.md#inventory)
- [Publish](artist_tools.md#publisher)
- [Library Loader](artist_tools.md#library-loader)

## Publishing Alembic Cameras
You can publish baked camera in Alembic format. Select your camera and go **OpenPype -> Create** and select **Camera (abc)**.
This will create Alembic ROP in **out** with path and frame range already set. This node will have a name you've
assigned in the **Creator** menu. For example if you name the subset `Default`, output Alembic Driver will be named
`cameraDefault`. After that, you can **OpenPype -> Publish** and after some validations your camera will be published
to `abc` file.

## Publishing Composites - Image Sequences
You can publish image sequence directly from Houdini. You can use any `cop` network you have and publish image
sequence generated from it. For example I've created simple **cop** graph to generate some noise:
![Noise COP](assets/houdini_imagesequence_cop.png)

If I want to publish it, I'll select node I like - in this case `radialblur1` and go **OpenPype -> Create** and
select **Composite (Image Sequence)**. This will create `/out/imagesequenceNoise` Composite ROP (I've named my subset
*Noise*) with frame range set. When you hit **Publish** it will render image sequence from selected node.

## Publishing Point Caches (alembic)
Publishing point caches in alembic format is pretty straightforward, but it is by default enforcing better compatibility
with other DCCs, so it needs data do be exported prepared in certain way. You need to add `path` attribute so objects
in alembic are better structured. When using alembic round trip in Houdini (loading alembics, modifying then and
then publishing modifications), `path` is automatically resolved by alembic nodes.

In this example, I've created this node graph on **sop** level, and I want to publish it as point cache.

![Pointcache setup](assets/houdini_pointcache_path.png)

*Note: `connectivity` will add index for each primitive and `primitivewrangle1` will add `path` attribute, so it will
be for each primitive (`sphere1` and `sphere2`) as Maya is expecting - `strange_GRP/strange0_GEO/strange0_GEOShape`. How
you handle `path` attribute is up to you, this is just an example.*

Now select the `output0` node and go **OpenPype -> Create** and select **Point Cache**. It will create
Alembic ROP `/out/pointcacheStrange`


## Redshift
:::note Work in progress
This part of documentation is still work in progress.
:::

## USD (experimental support)
### Publishing USD
You can publish your Solaris Stage as USD file.
![Solaris USD](assets/houdini_usd_stage.png)

This is very simple test stage. I've selected `output` **lop** node and went to **OpenPype -> Create** where I've
selected **USD**. This created `/out/usdDefault` USD ROP node.

### Publishing USD render

USD Render works in similar manner as USD file, except it will create **USD Render** ROP node in out and will publish
images produced by it. If you have selected node in Solaris Stage it will by added as **lop path** to ROP.

## Publishing VDB

Publishing VDB files works as with other data types. In this example I've created simple PyroFX explosion from
sphere. In `pyro_import` I've converted the volume to VDB:

![VDB Setup](assets/houdini_vdb_setup.png)

I've selected `vdb1` and went **OpenPype -> Create** and selected **VDB Cache**. This will create
geometry ROP in `/out` and sets its paths to output vdb files. During the publishing process
whole dops are cooked.
