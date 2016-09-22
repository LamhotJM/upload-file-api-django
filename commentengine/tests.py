from django.test import TestCase
from models import *
import datetime


class CommentSetup(TestCase):
    def _create_comment(self):
        self.comment = MasterComment.objects.create(commentid=1, userid='1', loanid='1', comment='Comment Lorem Ipsum',
                                                    file_upload='Upload.png', context_id=1, context_scope='Lorem Ipsum',
                                                    status=1, createdby='Lorem Ipsum',
                                                    createddate='2038-01-19 03:14:07',
                                                    createdfrom='Lorem Ipsum',
                                                    modifiedby='Lorem Ipsum',
                                                    modifiedfrom="Lorem Ipsum", modifieddate='2038-01-19 03:14:07')

    def setUp(self):
        self._create_comment()


class CommentTest(CommentSetup):
    def setUp(self):
        """To test a player attacking a monster, a game must first be set up."""
        super(CommentTest, self).setUp()

    def test_comment(self):
        """Tests that attack arithmetic is correct."""
        comment = MasterComment.objects.get(commentid=1)
        t1 = 'Test 001 Comment Id match'
        print t1
        self.assertEqual(comment.commentid, 1)
        t2 = 'Test 002 user id match '
        print t2
        self.assertEqual(comment.userid, '1')
        t3 = 'Test 003 loan id match '
        print t3
        self.assertEqual(comment.loanid, '1')
        t4 = 'Test 004 comment match '
        print t4
        self.assertEqual(comment.comment, 'Comment Lorem Ipsum')
        t5 = 'Test 005  file upload match '
        print t5
        self.assertEqual(comment.file_upload, 'Upload.png')
        t6 = 'Test 006 contex id match '
        print t6
        self.assertEqual(comment.context_id, 1)
        t7 = 'Test 007 contex scope match '
        print t7
        self.assertEqual(comment.context_scope, 'Lorem Ipsum')
        t8 = 'Test 008 status match'
        print t8
        self.assertEqual(comment.status, 1)
        t9 = 'Test 009 createdby match '
        print t9
        self.assertEqual(comment.createdby, 'Lorem Ipsum')

        t10 = 'Test 010 created from match '
        print t10
        self.assertEqual(comment.createdfrom, 'Lorem Ipsum')
        t11 = 'Test 011  created date match'
        print t11
        self.assertEqual(comment.modifiedby, 'Lorem Ipsum')
        t12 = 'Test 0013 modifiedfrom match '
        print t12
        self.assertEqual(comment.modifiedfrom, 'Lorem Ipsum')
